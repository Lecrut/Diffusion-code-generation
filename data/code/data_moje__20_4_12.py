def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 15, 42, -3, -10]
    for value in test_values:
        print(value, is_even(value))