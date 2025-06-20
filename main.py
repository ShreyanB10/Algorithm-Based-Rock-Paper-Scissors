rock_count: int = 0
paper_count: int = 0
scissors_count: int = 0
counts_list: list[int] = [rock_count,paper_count,scissors_count]
options_list: list[str] = ["rock", "paper", "scissors"]
computer_wins: int = 0
user_wins: int = 0
ties: int = 0
total_games: int = 0
user_win_perc: float = 0

def rps(user: str,computer: str) -> None:
    global rock_count,paper_count,scissors_count,counts_list,computer_wins,user_wins,ties,total_games

    if user == "quit":
        quit()
    elif user == "paper":
        total_games += 1
        paper_count += 1
        if computer == "rock":
            user_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You win! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == "scissors":
            computer_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You lose! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == user:
            ties += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"We tied! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
    elif user == "rock":
        total_games += 1        
        rock_count += 1
        if computer == "paper":
            computer_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You lose! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == "scissors":
            user_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You win! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == user:
            ties += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"We tied! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
    elif user == "scissors":
        total_games += 1
        scissors_count += 1
        if computer == "rock":
            computer_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You lose! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == "paper":
            user_wins += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"You win! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
        elif computer == user:
            ties += 1
            user_win_perc = round(((user_wins / total_games)*100),1)
            print(f"We tied! I played {computer} and you played {user}! Record: {user_wins}-{computer_wins}-{ties} Win Rate: {user_win_perc}%\n")
    else:
        print("Error! Please try again!")
        rps(input("rock, paper, or scissors? "),options_list[counts_list.index(max(counts_list)) - 2])

    counts_list = [rock_count,paper_count,scissors_count]

def main() -> None:
    while True:
        rps(input("rock, paper, or scissors? "),options_list[counts_list.index(max(counts_list)) - 2])

if __name__ == '__main__':
    main()