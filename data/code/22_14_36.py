def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_values = [-10, -5, -3, -1, 0, 1, 3, 5, 7, 9]
    for value in test_values:
        print(f"{value} is odd: {is_odd(value)}")