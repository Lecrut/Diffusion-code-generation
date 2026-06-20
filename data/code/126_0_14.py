def is_equal(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (10, 5),
        ("hello", "hello"),
        (1, 2)
    ]
    
    for a, b in test_cases:
        print(is_equal(a, b))