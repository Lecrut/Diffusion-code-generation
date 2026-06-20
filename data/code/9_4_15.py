def safe_strip(value):
    if value is None:
        return None
    if not isinstance(value, str):
        try:
            str_value = str(value)
            return str_value.strip()
        except Exception:
            return None
    return value.strip()

if __name__ == '__main__':
    test_cases = [
        "  hello world  ",
        "   ",
        42,
        None,
        ["a", "b"],
        3.14,
        "   \n\t   ",
    ]
    for case in test_cases:
        result = safe_strip(case)
        print(result)