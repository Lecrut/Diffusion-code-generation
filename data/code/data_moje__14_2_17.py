def get_third_value(t):
    if not t:
        raise ValueError('Tuple is empty')
    if len(t) < 3:
        raise ValueError('Tuple has fewer than three elements')
    return t[2]
if __name__ == '__main__':
    sample_tuple = (1, 2, 3, 4, 5)
    result = get_third_value(sample_tuple)
    print(f'Third value of {sample_tuple} is: {result}')
    another_tuple = ('a', 'b', 'c')
    result2 = get_third_value(another_tuple)
    print(f'Third value of {another_tuple} is: {result2}')
    try:
        empty_tuple = ()
        get_third_value(empty_tuple)
    except ValueError as e:
        print(f'Error: {e}')
    try:
        short_tuple = (1, 2)
        get_third_value(short_tuple)
    except ValueError as e:
        print(f'Error: {e}')