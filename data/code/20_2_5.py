def is_even(number):
    if not isinstance(number, (int, float)):
        raise TypeError('Input must be a number')
    return number % 2 == 0
if __name__ == '__main__':
    sample_values = [2, 3, 4, 5, 0, -2, -3, 100, 99]
    results = [is_even(value) for value in sample_values]
    for value, result in zip(sample_values, results):
        print(f'{value}: {result}')