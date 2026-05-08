def evaluate_condition(condition_string):
    if not condition_string:
        return False
    parts = condition_string.lower().split()
    if len(parts) == 0:
        return False
    result = False
    for part in parts:
        if part == 'and':
            continue
        elif part == 'or':
            continue
        else:
            try:
                value = part in ('true', 't', 'yes')
                if value:
                    result = result or True
                else:
                    result = result and True
            except Exception:
                pass
    return result
if __name__ == '__main__':
    test_cases = [
        ("A and B", True),
        ("A or B", True),
        ("not A", False),
        ("B and not A", False),
        ("A and not B", False),
        ("A or B or C", True),
        ("A and B and C", False),
        ("A and B and A", True),
        ("invalid syntax", None),
        ("", False),
        ("A and", None)
    ]
    for input_str, expected in test_cases:
        actual = evaluate_condition(input_str)
        status = "PASS" if actual == expected else f"FAIL (Expected: {expected}, Got: {actual})"
        print(f"Input: '{input_str}' -> Result: {actual} [{status}]")