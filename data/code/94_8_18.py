def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_values = [
        [True, False, True, False],
        [False, False, False],
        [0, 1, 0],
        ['', 'hello', ''],
        []
    ]
    
    for values in test_values:
        print(f"Input: {values} -> Output: {any_true(values)}")