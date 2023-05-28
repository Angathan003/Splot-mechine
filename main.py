import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {"A": 2, "B": 4, "C": 6, "D": 8}
symbol_value = {"A": 5, "B": 4, "C": 3, "D": 2}


def deposit():
    while True:
        amount = input("What would you like to deposit? $")
        if amount.isdigit() and int(amount) > 0:
            return int(amount)
        else:
            print("Please enter a positive number.")


def get_number_of_lines():
    while True:
        lines = input(f"Enter the number of lines to bet on (1-{MAX_LINES}): ")
        if lines.isdigit() and 1 <= int(lines) <= MAX_LINES:
            return int(lines)
        else:
            print("Enter a valid number of lines.")


def get_bet():
    while True:
        amount = input(f"What would you like to bet on each line? (${MIN_BET}-${MAX_BET}): ")
        if amount.isdigit() and MIN_BET <= int(amount) <= MAX_BET:
            return int(amount)
        else:
            print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")


def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        if all(symbol == column[line] for column in columns):
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = [symbol for symbol, count in symbols.items() for _ in range(count)]
    return [random.sample(all_symbols, rows) for _ in range(cols)]


def print_slot_machine(columns):
    for row in zip(*columns):
        print(" | ".join(row))


def spin(balance):
    lines = get_number_of_lines()
    total_bet = 0
    while not MIN_BET <= total_bet <= balance:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is: ${balance}")
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print("You won on lines:", *winning_lines)
    return winnings - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")


main()
