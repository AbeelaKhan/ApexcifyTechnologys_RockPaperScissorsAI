import random

user_history = []

move_counts = {
    "rock": 0,
    "paper": 0,
    "scissors": 0
}

MOVES = ["rock", "paper", "scissors"]

WINS = {
    "rock": "scissors",
    "paper": "rock",
    "scissors": "paper"
}

def ai_choice():
    if len(user_history) < 3:
        return random.choice(MOVES)

    if random.random() < 0.3:
        return random.choice(MOVES)

    if random.random() < 0.6:
        most_used = max(move_counts, key=move_counts.get)
        for move in WINS:
            if WINS[move] == most_used:
                return move

    last_move = user_history[-1]
    for move in WINS:
        if WINS[move] == last_move:
            return move

    return random.choice(MOVES)

def get_winner(user, ai):
    if user == ai:
        return "tie"
    elif WINS[user] == ai:
        return "user"
    else:
        return "ai"

def play_game():
    user_score = 0
    ai_score = 0
    ties = 0
    round_num = 1

    print("\n" + "="*40)
    print("   ROCK - PAPER - SCISSORS")
    print("="*40)
    print("Type rock, paper, or scissors")
    print("Type quit to exit\n")

    while True:
        print(f"--- Round {round_num} ---")
        print(f"You: {user_score}  AI: {ai_score}  Ties: {ties}")

        user = input("Your move: ").strip().lower()

        if user == "quit":
            print("\nFinal Score:")
            print(f"You: {user_score}  AI: {ai_score}  Ties: {ties}")
            break

        if user not in MOVES:
            print("Invalid move\n")
            continue

        user_history.append(user)
        move_counts[user] += 1

        ai = ai_choice()
        print("AI chose:", ai)

        result = get_winner(user, ai)

        if result == "tie":
            print("Tie\n")
            ties += 1
        elif result == "user":
            print("You win\n")
            user_score += 1
        else:
            print("AI wins\n")
            ai_score += 1

        round_num += 1

play_game()