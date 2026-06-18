def determine_sign(value):
    try:
        if isinstance(value, (int, float)):
            return 1 if value > 0 else (-1 if value < 0 else 0)
        raise TypeError(f"Unsupported type {type(value).__name__}")
    except Exception as e:
        print(f"Error processing input: {e}")
        return None
if __name__ == '__main__':
    test_cases = [5, -3.5, 0, "invalid", None]
    for case in test_cases:
        result = determine_sign(case)
        if result is not None:
            print(f"Sign of {case}: {result}")