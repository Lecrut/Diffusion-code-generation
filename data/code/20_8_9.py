def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 2, -2, 4, -4, 1, -1, 5]
    for value in test_values:
        result = is_even(value)
        print(result)