def strip_whitespace(value):
    if value is None:
        return ""
    if not isinstance(value, str):
        value = str(value)
    return value.strip()

if __name__ == '__main__':
    sample_values = [
        "  hello world  ",
        None,
        42,
        3.14,
        ["a", "b"],
        "  \t\n  spaced  \t\n  "
    ]
    for val in sample_values:
        result = strip_whitespace(val)
        print(result)