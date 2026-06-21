def check_inequality(a, b):
    type_differs = type(a) is not type(b)
    value_differs = a != b if not type_differs else True
    return type_differs or value_differs

if __name__ == '__main__':
    test_cases = [
        (5, 10),
        (5.0, 10.0),
        ('hello', 'world'),
        ([1, 2], [1, 2]),
        ({'a': 1}, {'b': 2}),
        (True, False),
        (None, None),
        (1 + 2j, 3 + 4j)
    ]
    
    for idx, (value_a, value_b) in enumerate(test_cases):
        result = check_inequality(value_a, value_b)
        print(f"Test Case {idx + 1}: check_inequality({value_a!r}, {value_b!r}) = {result}")