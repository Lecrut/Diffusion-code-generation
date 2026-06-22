def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [4, 7, 10, 15, 0, -2, -5]
    for value in test_values:
        result = is_even(value)
        print(result)