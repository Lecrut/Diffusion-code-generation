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
        (3.14, 3.14),
        (True, False)
    ]

    for val1, val2 in sample_values:
        result = verify_equality(val1, val2)
        print(f"verify_equality({val1}, {val2}) = {result}")