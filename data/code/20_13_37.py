def verify_equality(var1, var2):
    if type(var1) != type(var2):
        return False
    return var1 == var2

if __name__ == '__main__':
    sample_values = [
        (5, 5),
        (3.14, 3.14),
        ("hello", "hello"),
        ([1, 2, 3], [1, 2, 3]),
        ({'a': 1}, {'a': 1}),
        (True, False),
        (None, None),
        (5, "5"),
        (3.14, "3.14"),
        ([1, 2, 3], [3, 2, 1])
    ]

    for var1, var2 in sample_values:
        result = verify_equality(var1, var2)
        print(f"verify_equality({var1}, {var2}) = {result}")