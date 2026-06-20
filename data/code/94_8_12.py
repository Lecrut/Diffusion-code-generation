def any_true(iterable):
    return any(iterable)

if __name__ == '__main__':
    test_values = [
        [True, False, True, False],
        [False, False, False, False],
        [1, 0, '', None],
        [],
        ['hello', 'world']
    ]
    
    results = {tuple(values): any_true(values) for values in test_values}
    
    for input_values, result in results.items():
        print(f"Input: {input_values} -> Output: {result}")