def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [2, 3, 0, 15, 100]
    for value in test_values:
        print(is_even(value))