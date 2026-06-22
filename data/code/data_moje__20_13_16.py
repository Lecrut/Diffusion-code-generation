def is_even(number):
    even_samples = {0, 2, 4, 6, 8, 10, -2, -4, -6, -8, -10}
    return number % 2 == 0 and number in even_samples

if __name__ == '__main__':
    test_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -1, -2, -3]
    for value in test_values:
        result = is_even(value)
        print(f"{value}: {result}")