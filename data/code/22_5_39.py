def check_odd_or_even(number):
    return "Even" if number % 2 == 0 else "Odd"

if __name__ == '__main__':
    test_values = [-10, -5, -1, 0, 1, 5, 10]
    for value in test_values:
        print(f"{value} is {check_odd_or_even(value)}")