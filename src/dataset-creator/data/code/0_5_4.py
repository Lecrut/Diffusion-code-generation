def evaluate_equality(a: object, b: object) -> bool:
    if a is None and b is None:
        return True
    elif a is not None and b is not None:
        return a == b
    else:
        return False
if __name__ == '__main__':
    test_cases = [
        (None, None),
        ("hello", "world"),
        (123, 456),
        ([], []),
        ({}, {}),
        (True, True),
        (False, False),
        (0.0, 0.0),
    ]
    for val_a, val_b in test_cases:
        result = evaluate_equality(val_a, val_b)
        print(f"evaluate_equality({val_a!r}, {val_b!r}) -> {result}")