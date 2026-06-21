def extract_third(t):
    if not isinstance(t, tuple):
        raise TypeError('Input must be a tuple')
    if len(t) < 3:
        raise ValueError('Tuple must have at least three elements')
    return t[2]
if __name__ == '__main__':
    sample_tuples = [(1, 2, 3, 4, 5), ('a', 'b', 'c'), (None, True, 'third')]
    for t in sample_tuples:
        result = extract_third(t)
        print(f'Third element of {t}: {result}')
    try:
        extract_third((1, 2))
    except ValueError as e:
        print(f'Error: {e}')
    try:
        extract_third([1, 2, 3])
    except TypeError as e:
        print(f'Error: {e}')