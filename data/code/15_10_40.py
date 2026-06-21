def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    SAMPLE_VALUES = [
        (10, 10),
        ("hello", "world"),
        ([1, 2, 3], [1, 2, 3]),
        ({"a": 1}, {"a": 1}),
        (5.0, 5),
        (True, False),
        ("test", "test")
    ]
    
    for a, b in SAMPLE_VALUES:
        print(check_equality(a, b))