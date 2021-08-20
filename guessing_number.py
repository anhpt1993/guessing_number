# guessing number
import random
def input_data():
    while True:
        try:
            num = int(input("Enter an integer in range (1,10): "))
            if 1 <= num <= 10:
                return num
                break
            else:
                print("Out of range! Try again please")
                print()
        except Exception:
            print("Value shall be an integer, not a decimal or string")
            print()

if __name__ == '__main__':
    computer_num = random.randint(1,10)
    player = []
    while True:
        num = input_data()
        player.append(num)
        if num == computer_num:
            print("------------------------")
            print("Computer number is {}".format(computer_num))
            print("You guess {}".format(player))
            print("You won! Congratulations")
            print("------------------------")
            exit()
        elif len(player) >= 3:
            print("--------------------------------")
            print("Computer number is {}".format(computer_num))
            print("You guess {}".format(player))
            print("You guessed more than 3 times!!!")
            print("You lose! Better luck next time")
            print("--------------------------------")
            break

