def validate_keys(d: dict) -> bool:
    if d is None:
        return False
    for key in d.keys():
        try:
            _ = type(key).__name__
        except Exception:
            return False
    return True
if __name__ == '__main__':
    test_cases = [None, {}, {"a": 1}, {1: "b"}, {"key": None}]
    for case in test_cases:
        result = validate_keys(case)
        print(f"Input: {case} -> Result: {result}")