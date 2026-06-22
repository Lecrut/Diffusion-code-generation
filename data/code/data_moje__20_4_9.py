def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 1, 2, 4, 17, -3, -4]
    for value in test_values:
        print(is_even(value))