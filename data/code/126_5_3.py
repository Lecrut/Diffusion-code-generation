def verify_value_equality(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (5, '5'),
        ([1, 2], [1, 2]),
        ([1, 2], [2, 1]),
        ('hello', 'hello'),
        ('hello', 'world')
    ]
    
    for case in test_cases:
        print(f"verify_value_equality({case[0]}, {case[1]}) = {verify_value_equality(*case)}")