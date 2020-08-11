import random


def get_score(name):
    read_file = open("rating.txt", "r")
    for record in read_file:
        if name in record:
            score = record.split(" ")[1].strip("\n")
            print(f"Your rating: {score}")
            read_file.close()
            return
    else:
        read_file.close()
        score = 0
        write_file = open("rating.txt", "a")
        write_file.write(f"{name} {score}\n")
        print(f"Your rating: 0")
        write_file.close()


def update_score(name_, score_):
    d = {}
    read_file = open("rating.txt", "r")
    for line in read_file:
        (name, score) = line.split()
        d[str(name)] = int(score)
    if name_ in d:
        d[name_] += int(score_)
    else:
        d[name_] = score_
    read_file.close()

    write_file = open("rating.txt", "w")
    for name_, score_ in d.items():
        write_file.write("%s %s\n" % (name_, score_))
    write_file.close()


def play():
    default_options = ["scissors", "paper", "rock"]
    player_name = input("Enter your name: ")
    print(f"Hello, {player_name}")
    player_options = input().split(',')
    is_default = True

    if len(player_options) > 1:
        print("Okay, let's start")
        is_default = False
        default_options = player_options

    while True:
        computer_choice = random.choice(default_options)
        player_choice = input()

        if player_choice in default_options:
            if not is_default:
                total_length = len(default_options)
                half_length = total_length // 2

                if default_options[default_options.index(player_choice)] != default_options[half_length]:
                    if default_options[default_options.index(player_choice)] < default_options[half_length]:
                        move_right = half_length - (default_options.index(player_choice))
                        default_options = default_options[-move_right:] + default_options[:-move_right]
                    else:
                        move_left = (default_options.index(player_choice)) - half_length
                        default_options = default_options[move_left:] + default_options[:move_left]
            if player_choice == computer_choice:
                print(f"There is a draw ({computer_choice})")
                update_score(player_name, "50")
            else:
                if is_default:
                    if player_choice == default_options[0] and computer_choice == default_options[2] \
                            or player_choice == default_options[1] and computer_choice == default_options[0] \
                            or player_choice == default_options[2] and computer_choice == default_options[1]:
                        print(f"Sorry, but computer chose {computer_choice}")
                    else:
                        print(f"Well done. Computer chose {computer_choice} and failed")
                        update_score(player_name, "100")
                else:
                    if default_options.index(player_choice) > default_options.index(computer_choice):
                        print(f"Well done. Computer chose {computer_choice} and failed")
                        update_score(player_name, "100")
                    else:
                        print(f"Sorry, but computer chose {computer_choice}")
        elif player_choice == "!exit":
            print("Bye!")
            break
        elif player_choice == "!rating":
            get_score(player_name)
        else:
            print("Invalid input")


play()
        # Test values
        # rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors,fire
