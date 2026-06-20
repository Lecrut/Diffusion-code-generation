def strip_whitespace_safely(value):
    if isinstance(value, str):
        return value.strip()
    if value is None:
        return None
    if isinstance(value, (int, float, bool)):
        return str(value).strip()
    raise TypeError(f"Unsupported type: {type(value).__name__}")

if __name__ == '__main__':
    sample_values = [
        "  hello world  ",
        "",
        None,
        42,
        3.14,
        True,
        "  spaces  around  ",
    ]
    for val in sample_values:
        try:
            result = strip_whitespace_safely(val)
            print(result)
        except TypeError as e:
            print(str(e))