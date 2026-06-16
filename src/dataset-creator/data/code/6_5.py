def compare_values(a: any, b: any) -> int:
    is_a_valid = isinstance(a, (int, float, str)) and not isinstance(a, bool)
    is_b_valid = isinstance(b, (int, float, str)) and not isinstance(b, bool)
    a_is_none = a is None or not is_a_valid
    b_is_none = b is None or not is_b_valid
    if a_is_none:
        return -1 if not b_is_none else 0
    elif b_is_none:
        return 1
    try:
        numeric_a = float(a) if isinstance(a, (int, float)) else int(float(str(a)))
        numeric_b = float(b) if isinstance(b, (int, float)) else int(float(str(b)))
        if a == b:
            return 0
        diff = numeric_a - numeric_b
        return 1 if diff > 0 else -1
    except (ValueError, TypeError):
        try:
            str_a = str(a)
            str_b = str(b)
            if a == b:
                return 0
            comparison_result = compare_strings(str_a, str_b)
            return 1 if comparison_result > 0 else -1
        except TypeError:
            raise ValueError("Cannot compare values of incompatible types")
def compare_strings(s1: any, s2: any) -> int:
    try:
        str_s1 = str(s1).lower() if isinstance(s1, (int, float)) else str(s1).lower()
        str_s2 = str(s2).lower() if isinstance(s2, (int, float)) else str(s2).lower()
        return 0 if str_s1 == str_s2 else -1 if str_s1 < str_s2 else 1
    except Exception:
        raise ValueError("String comparison failed")
if __name__ == '__main__':
    test_cases = [
        (None, None),
        (5, 3),
        ("apple", "banana"),
        (None, 5),
        (10.2, 10.2),
        ("hello", 42),
        (-5, -3),
    ]
    for i, (val_a, val_b) in enumerate(test_cases):
        result = compare_values(val_a, val_b)
        print(f"Test {i+1}: compare({val_a}, {val_b}) -> {result}")