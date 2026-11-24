import random


def get_number(msg):
    while True:
        n = input(msg)
        if n.isdigit() and 1 <= int(n) <= 6:
            return int(n)
        print("Pick a number from 1 to 6!")


def innings(batting, target=None):
    # batting = "you" or "cpu"
    score = 0
    while True:
        if batting == "you":
            mine = get_number("Your shot (1-6): ")
            cpu = random.randint(1, 6)
            print("CPU bowled", cpu)
        else:
            mine = get_number("Your bowl (1-6): ")
            cpu = random.randint(1, 6)
            print("CPU played", cpu)

        if mine == cpu:
            print("OUT!")
            return score
        score += mine if batting == "you" else cpu
        print("Score:", score)
        if target and score >= target:
            return score


def main():
    print("--- Hand Cricket ---")
    toss = input("Odd or even? (o/e): ").lower()
    num = get_number("Throw a number (1-6): ")
    cpu = random.randint(1, 6)
    total = num + cpu
    print("CPU threw", cpu, "- total is", total)

    won = (total % 2 == 1) == (toss == "o")
    if won:
        choice = input("You won the toss! bat or bowl? ").lower()
    else:
        choice = random.choice(["bat", "bowl"])
        print("CPU won the toss and chose to", choice)
        choice = "bowl" if choice == "bat" else "bat"  # what you do

    if choice == "bat":
        print("\nYou bat first")
        s1 = innings("you")
        print("\nTarget for CPU:", s1 + 1)
        s2 = innings("cpu", s1 + 1)
    else:
        print("\nCPU bats first")
        s2 = innings("cpu")
        print("\nTarget for you:", s2 + 1)
        s1 = innings("you", s2 + 1)

    print("\nYou:", s1, "| CPU:", s2)
    if s1 > s2:
        print("You win!")
    elif s2 > s1:
        print("CPU wins!")
    else:
        print("It's a tie!")


main()