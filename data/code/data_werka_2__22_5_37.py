EVEN = "Even"
ODD = "Odd"

def check_parity(number):
    remainder = number % 2
    return EVEN if remainder == 0 else ODD

if __name__ == '__main__':
    test_values = [-10, -5, -1, 0, 1, 5, 10, 15]
    for value in test_values:
        parity = check_parity(value)
        print(f"The number {value} is {parity}.")