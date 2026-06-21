def is_even(number):
    if not isinstance(number, int):
        raise TypeError('Input must be an integer')
    return number % 2 == 0
if __name__ == '__main__':
    test_values = [-4, -3, 0, 3, 4, 100, -100]
    for val in test_values:
        result = is_even(val)
        print(f'{val}: {result}')