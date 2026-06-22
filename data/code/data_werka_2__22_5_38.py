def check_odd_or_even(number):
    remainder = number % 2
    if remainder == 0:
        return "Even"
    else:
        return "Odd"

if __name__ == '__main__':
    test_numbers = [-10, -5, -3, -1, 0, 2, 4, 6, 8, 10]
    for num in test_numbers:
        result = check_odd_or_even(num)
        print(f"The number {num} is {result}.")