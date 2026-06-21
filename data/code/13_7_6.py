def to_camel_case(text):
    if not text:
        return text
    parts = text.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
        else:
            result += '_'
    return result

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_example", "snakeCaseExample"),
        ("a_b_c", "aBC"),
        ("alreadyCamel", "alreadyCamel"),
        ("single", "single"),
        ("", ""),
        ("with__double_underscores", "with__doubleUnderscores"),
        ("trailing_", "trailing_"),
        ("_leading", "_leading"),
        ("__both__", "__both__")
    ]
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        print(f"{input_val} -> {result}")
        if result != expected:
            print(f"FAILED: expected {expected}, got {result}")