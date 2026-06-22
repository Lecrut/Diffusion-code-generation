def get_third_value(t: tuple) -> object:
    if not isinstance(t, tuple):
        raise TypeError('Input must be a tuple')
    if len(t) < 3:
        raise ValueError('Tuple must have at least three elements')
    return t[2]
if __name__ == '__main__':
    sample_tuples = [(1, 2, 3, 4, 5), ('a', 'b', 'c'), (None, None, None), (10, 20, 30)]
    for t in sample_tuples:
        try:
            result = get_third_value(t)
            print(f'Third value of {t}: {result}')
        except (ValueError, TypeError) as e:
            print(f'Error: {e}')
    try:
        get_third_value((1, 2))
    except ValueError as e:
        print(f'Caught expected error: {e}')
    try:
        get_third_value('not a tuple')
    except TypeError as e:
        print(f'Caught expected error: {e}')