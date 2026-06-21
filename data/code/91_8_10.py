def validate_and_negate(flag):
    if not isinstance(flag, bool):
        raise ValueError("Input must be a boolean value")
    return not flag

if __name__ == '__main__':
    test_cases = [True, False]
    for case in test_cases:
        try:
            result = validate_and_negate(case)
            print(f"Original: {case} | Negated: {result}")
        except ValueError as e:
            print(f"Error processing {case}: {e}")