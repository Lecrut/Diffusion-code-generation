def to_camel_case(text):
    if not text:
        return text
    if '_' not in text:
        return text
    parts = text.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return result

if __name__ == '__main__':
    test_cases = [
        ("snake_case_example", "snakeCaseExample"),
        ("hello_world", "helloWorld"),
        ("a", "a"),
        ("", ""),
        ("no_underscore_here", "noUnderscoreHere"),
        ("multiple___underscores", "multipleUnderscores"),
        ("trailing_", "trailing"),
        ("_leading", "Leading"),
        ("_both_", "Both"),
    ]
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        print(result)