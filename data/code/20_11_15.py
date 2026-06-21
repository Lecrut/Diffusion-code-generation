def is_even(number):
    return number % 2 == 0

if __name__ == '__main__':
    test_values = [0, 2, -2, 4, -4, 1, -1, 100, -100]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")