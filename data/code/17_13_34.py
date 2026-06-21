def is_even(number):
    return number & 1 == 0

if __name__ == '__main__':
    test_values = [0, 2, -4, 3, 5, -7]
    for value in test_values:
        print(is_even(value))