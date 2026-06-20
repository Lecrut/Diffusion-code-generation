def safe_strip(value):
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return ""
    return str(value).strip()

if __name__ == '__main__':
    test_values = [
        "  hello world  ",
        12345,
        3.14,
        None,
        ["not", "a", "string"],
        "   ",
        True
    ]
    for val in test_values:
        result = safe_strip(val)
        print(f"Input: {repr(val)} -> Output: {repr(result)}")