def strip_whitespace_safely(value):
    if not isinstance(value, str):
        return None
    return value.strip()

if __name__ == '__main__':
    sample_values = [
        "  hello world  ",
        42,
        None,
        "no_extra_space",
        "   ",
        [],
        {"key": "value"}
    ]
    results = [strip_whitespace_safely(v) for v in sample_values]
    for original, result in zip(sample_values, results):
        print(f"Input: {repr(original)}, Output: {repr(result)}")