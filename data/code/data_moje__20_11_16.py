def is_even(n):
    if not isinstance(n, int):
        raise TypeError('Input must be an integer.')
    return n % 2 == 0
if __name__ == '__main__':
    sample_values = [0, 1, 2, -1, -2, -3, 10, 11]
    for value in sample_values:
        result = is_even(value)
        print(f'is_even({value}) = {result}')