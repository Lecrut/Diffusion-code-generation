def are_equal(var1, var2):
    return type(var1) == type(var2) and var1 == var2

if __name__ == '__main__':
    sample_values = [
        (42, 42),
        ('hello', 'world'),
        ([1, 2, 3], [1, 2, 3]),
        ({'a': 1}, {'a': 1}),
        (3.14, 3.14),
        (True, False)
    ]

    for val1, val2 in sample_values:
        print(are_equal(val1, val2))