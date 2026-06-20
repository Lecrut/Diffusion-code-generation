def verify_value_equality(a, b):
    return a == b

if __name__ == '__main__':
    test_values = {
        (5, 5): True,
        (5, '5'): False,
        ([1, 2], [1, 2]): True,
        ([1, 2], [2, 1]): False,
        ('hello', 'hello'): True,
        ('hello', 'world'): False
    }
    
    for values, expected in test_values.items():
        result = verify_value_equality(*values)
        print(f"verify_value_equality({values[0]}, {values[1]}) = {result}, Expected: {expected}")