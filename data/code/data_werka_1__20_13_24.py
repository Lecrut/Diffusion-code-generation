def verify_equality(var1, var2):
    if type(var1) != type(var2):
        return False
    return var1 == var2

if __name__ == '__main__':
    sample_values = [
        (5, 5),
        ('hello', 'world'),
        ([1, 2, 3], [1, 2, 3]),
        ({'a': 1}, {'a': 1}),
        (4.0, 4),
        (True, 1)
    ]

    for val1, val2 in sample_values:
        result = verify_equality(val1, val2)
        print(f"verify_equality({val1}, {val2}) = {result}")