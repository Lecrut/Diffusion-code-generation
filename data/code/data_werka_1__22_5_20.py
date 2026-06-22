def is_odd_or_even(number):
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    sample_values = [0, 1, 2, 3, 4, 5, -1, -2]
    for value in sample_values:
        result = is_odd_or_even(value)
        print(f"{value} is {result}")