def is_zero(x):
    return x == 0

if __name__ == '__main__':
    test_cases = [
        (5, False),
        (-3, False),
        (0.0, True),
        (0j, True)
    ]

    for value, expected in test_cases:
        result = is_zero(value)
        print(f"is_zero({value!r}) -> {result} (expected: {expected})")