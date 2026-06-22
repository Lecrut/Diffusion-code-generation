def check_odd_or_even(number):
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    sample_values = [10, 7, 0, -3, 42]
    for value in sample_values:
        result = check_odd_or_even(value)
        print(f"{value} is {result}")