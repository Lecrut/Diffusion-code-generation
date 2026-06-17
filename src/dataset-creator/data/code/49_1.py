def determine_sign(value):
    if isinstance(value, (int, float)) and not isinstance(value, bool):
        return 1 if value > 0 else -1 if value < 0 else 0
    elif isinstance(value, str) or value is None:
        try:
            num = float(value)
            return determine_sign(num)
        except (ValueError, TypeError):
            pass
    raise ValueError(f"Unsupported type for sign determination: {type(value)}")
if __name__ == '__main__':
    test_cases = [10.5, -3, 0, "42", None]
    results = []
    for case in test_cases:
        try:
            result = determine_sign(case)
            results.append(f"{case} -> {result}")
        except ValueError as e:
            results.append(f"{case} -> Error: {e}")
    print("\n".join(results))