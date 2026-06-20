def any_true(iterable):
    if not isinstance(iterable, (list, tuple, set, range)):
        raise ValueError('Input must be an iterable')
    return any(iterable)
if __name__ == '__main__':
    test_values = [False, False, True]
    print(any_true(test_values))
    test_values = [0, 0, 0]
    print(any_true(test_values))
    test_values = ['', '', 'hello']
    print(any_true(test_values))
    test_values = []
    print(any_true(test_values))