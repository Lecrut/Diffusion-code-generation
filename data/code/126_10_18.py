def check_equality(a, b):
    return a == b

if __name__ == '__main__':
    test_cases = [
        (5, 5),
        (10, 5),
        ("hello", "hello"),
        (10.5, 10.5),
        (10, 10.0)
    ]
    
    for a, b in test_cases:
        print(f"check_equality({a}, {b}) = {check_equality(a, b)}")