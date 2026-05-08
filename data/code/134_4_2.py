def validate_exclusivity(conditions):
    n = len(conditions)
    for i in range(n):
        for j in range(i + 1, n):
            if conditions[i] and conditions[j]:
                return False
    return True
if __name__ == '__main__':
    test_cases = [
        ([False, False, False], True),
        ([True, False, False], True),
        ([False, True, False], True),
        ([True, True, False], False),
        ([True, True, True], False),
        ([False, False], True),
        ([True], True),
        ([], True),
        ([True, False, True], False),
        ([False, True, False, True], False)
    ]
    for conditions, expected in test_cases:
        result = validate_exclusivity(conditions)
        assert result == expected, f"Input: {conditions}, Expected: {expected}, Got: {result}"
        print(f"Test passed for {conditions}: Result = {result}")