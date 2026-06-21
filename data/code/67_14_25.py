def sum_two_numbers(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError('Both inputs must be either integers or floating-point numbers.')
    return a + b

if __name__ == '__main__':
    test_cases = {
        'case1': {'a': 5, 'b': 3},
        'case2': {'a': 2.5, 'b': 4.7},
        'case3': {'a': -1, 'b': -1},
        'case4': {'a': 0, 'b': 0},
        'case5': {'a': 100, 'b': 200.5}
    }
    
    for case, values in test_cases.items():
        result = sum_two_numbers(values['a'], values['b'])
        print(f"Result of adding {values['a']} and {values['b']}: {result}")