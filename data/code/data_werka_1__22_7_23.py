def is_odd(number):
    return number % 2 != 0

if __name__ == '__main__':
    test_values = [0, 1, -1, 2, -2, 3, -3, 4, -4]
    for value in test_values:
        print(f"{value} is odd: {is_odd(value)}")