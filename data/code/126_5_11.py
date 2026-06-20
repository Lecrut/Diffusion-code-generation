def verify_value_equality(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = {
        (5, 5): True,
        (5, '5'): False,
        ([1, 2], [1, 2]): True,
        ([1, 2], [2, 1]): False,
        ('hello', 'hello'): True,
        ('hello', 'world'): False
    }
    
    for case, expected in test_cases.items():
        result = verify_value_equality(*case)
        print(f"verify_value_equality({case[0]}, {case[1]}) = {result}, Expected: {expected}")