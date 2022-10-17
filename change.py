from cs50 import get_float

def main():
    cents = get_cents()

    quarters = calculate_quarters(cents)
    cents = cents - quarters * 25

    dimes = calculate_dimes(cents)
    cents = cents - dimes * 10

    nickels = calculate_nickels(cents)
    cents = cents - nickels * 5

    pennies = calculate_pennies(cents)
    cents = cents - pennies

    coins = quarters + dimes + nickels + pennies

    print(coins)

def get_cents():
    change = 0
    cents = 0
    while True:
        change = get_float("Enter amount of change owed: ")
        if change > 0:
            break
    cents = change * 100
    return cents

def calculate_quarters(cents):
    quarters = 0
    while (cents >= 25):
        quarters+=1
        cents = cents - 25
    return quarters

def calculate_dimes(cents):
    dimes = 0
    while (cents >= 10):
        dimes+=1
        cents = cents - 10
    return dimes

def calculate_nickels(cents):
    nickels = 0
    while (cents >= 5):
        nickels+=1
        cents = cents - 5
    return nickels

def calculate_pennies(cents):
    pennies = 0
    while (cents >= 1):
        pennies+=1
        cents = cents - 1
    return pennies

if __name__ == "__main__":
    main()