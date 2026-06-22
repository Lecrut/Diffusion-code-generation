def safe_strip(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        value = str(value)
    return value.strip()

if __name__ == '__main__':
    test_values = ["  hello  ", 42, "  world\n", None, 3.14, "\t\ndata\t\t"]
    for val in test_values:
        result = safe_strip(val)
        print(f"Input: {repr(val)} -> Output: {repr(result)}")