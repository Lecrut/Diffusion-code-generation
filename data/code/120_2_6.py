def are_values_equal(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = [
        (10, 10),
        ("hello", "hello"),
        (5.5, 5.5),
        (True, True),
        (1, 2),
        ([1, 2], [1, 2]),
        (None, None)
    ]
    
    for a, b in test_cases:
        print(f"{a} == {b}: {are_values_equal(a, b)}")