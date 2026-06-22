def determine_parity(number):
    remainder = number % 2
    return "Even" if remainder == 0 else "Odd"

if __name__ == '__main__':
    sample_values = [4, 7, 10, 15]
    for value in sample_values:
        print(f"{value} is {determine_parity(value)}")