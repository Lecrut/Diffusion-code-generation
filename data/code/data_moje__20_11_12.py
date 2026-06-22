def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -3, -1, 0, 1, 2, 7, 100]
    for value in test_values:
        print(is_even(value))