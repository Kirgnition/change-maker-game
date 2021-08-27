import random


def change(price, paid, total=False):
    # Takes value in cents and returns dictionary with the least amount of change
    currency = (50000, 20000, 10000, 5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)

    owed = paid - price
    change_dict = {}
    for c in currency:
        quotient, remainder = divmod(owed, c)
        if quotient == 0:
            continue
        else:
            change_dict[c] = quotient
            owed = remainder

    if total:
        return change_dict, paid - price
    else:
        return change_dict


def ppchange(changedict):
    # Print change in a pleasant way
    words = {50000: "500 euro",
             20000: "200 euro",
             10000: "100 euro",
             5000: "50 euro",
             2000: "20 euro",
             1000: "10 euro",
             500: "5 euro",
             200: "2 euro",
             100: "1 euro",
             50: "50 centesimi",
             20: "20 centesimi",
             10: "10 centesimi",
             5: "5 centesimi",
             2: "2 centesimi",
             1: "1 centesimi"}

    for n, v in changedict.items():
        print(f"{v} x {words[n]}")


items = {
    "popcorn piccoli": 250,
    "popcorn medi": 350,
    "popcorn grandi": 450,
    "popcorn extra grandi": 650,
    "acqua": 150,
    "bibita": 300,
    "patatine": 150,
    "caramelle": 100,
    "caffè": 100,
    "biglietto": 800,
    "biglietto ridotto": 600,
    "abbonamento": 3000,
}

# Main loop
n_round = 1
wins, losses = 0, 0
try:
    while True:
        # Create divider between rounds
        left_width, right_width = 20, 8
        print("".ljust(left_width + right_width, "="))
        print(f"Round {n_round}".ljust(2, " "), f"wins: {wins} losses: {losses}")
        print("".ljust(left_width + right_width, "="))

        # Generate a list of random items
        n_items = random.randint(1, 5)
        selected_items = []
        for i in range(n_items):
            selected_items.append(random.choice(list(items.items())))

        print("ITEMS REQUESTED".center(left_width + right_width, "-"))

        # Get total price and print a receipt
        price = 0
        for j, k in selected_items:
            price += k
            print(f"{j}".ljust(left_width, "."), f"{k/100:.2f} €".rjust(right_width), sep="")
        print("".ljust(left_width+right_width, "-"))
        print(f"Total".ljust(left_width, "."), f"{price/100:.2f} €".rjust(right_width), sep="")

        # Generate random amount as paid
        paid = random.randint(price, round((3*price) / 2))
        print(f"Paid".ljust(left_width, "."), f"{paid/100:.2f} €".rjust(right_width), sep="")

        # Compute change owed
        correct_change, total = change(price, paid, total=True)
        # Ask for user input
        guess = round(float(input("Type change owed in euros: "))*100)

        if guess == total:
            wins += 1
            print("CORRECT!")
            print(f"Change owed: {total/100:.2f} €")
            ppchange(correct_change)
        else:
            losses += 1
            print("WRONG")
            print(f"Change owed: {total/100:.2f} €")
            ppchange(correct_change)
        n_round += 1
except KeyboardInterrupt:
    exit()
