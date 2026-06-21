def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [-4, -1, 0, 1, 10]
    for val in test_values:
        print(is_even(val))