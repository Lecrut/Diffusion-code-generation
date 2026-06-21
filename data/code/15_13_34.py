def are_strictly_equal(value1, value2):
    return type(value1) is type(value2) and value1 == value2

if __name__ == '__main__':
    test_values = [
        (5, 5),
        ('hello', 'hello'),
        ([1, 2], [1, 2]),
        ((1, 2), (1, 2)),
        ({1, 2}, {1, 2}),
        ({'a': 1}, {'a': 1}),
        (3.14, 3.14),
        (True, True),
        (False, False),
        (None, None)
    ]
    
    for value1, value2 in test_values:
        result = are_strictly_equal(value1, value2)
        print(f"are_strictly_equal({value1}, {value2}) = {result}")