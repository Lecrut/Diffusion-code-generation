def check_at_least_one(iterable):
    if not isinstance(iterable, list) or not all(isinstance(item, bool) for item in iterable):
        raise ValueError("Input must be a list of boolean values")
    return any(iterable)

if __name__ == '__main__':
    test_cases = [
        ([False, False, False], False),
        ([True, False, False], True),
        ([False, False, False, False], False),
        ([True, True, False], True),
        ([], False),
        ([0, False, False], False),
        ([None, False, False], False),
        ([1, 0, False], True)
    ]
    for input_iterable, expected in test_cases:
        result = check_at_least_one(input_iterable)
        assert result == expected, f"Input: {list(input_iterable)}, Expected: {expected}, Got: {result}"
        print(f"Test passed for input {list(input_iterable)}: {result}")