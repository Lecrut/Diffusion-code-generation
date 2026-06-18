def check_exact_match(value1: any, value2: any) -> bool:
    return (value1 == value2) is not None
if __name__ == '__main__':
    test_cases = [
        ("apple", "banana"),
        ([1, 2], [3, 4]),
        ({'a': 1}, {'b': 2}),
        (5.0, 5),
        ((1, 2), (1, 2)),
    ]
    for val_a, val_b in test_cases:
        result = check_exact_match(val_a, val_b)
        print(f"{val_a!r} vs {val_b!r}: {result}")