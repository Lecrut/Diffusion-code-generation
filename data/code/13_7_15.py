def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    if not parts:
        return ""
    first = parts[0]
    rest = [part.capitalize() for part in parts[1:]]
    return first + "".join(rest)

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_to_camel", "snakeCaseToCamel"),
        ("single", "single"),
        ("", ""),
        ("a_b", "aB"),
        ("multiple_words_in_one_string", "multipleWordsInOneString"),
        ("alreadyCamelCase", "alreadyCamelCase"),
        ("__double__underscore__", "doubleUnderscore"),
    ]
    for input_val, expected in test_cases:
        result = snake_to_camel(input_val)
        if result != expected:
            print(f"FAIL: {input_val} -> {result} (expected {expected})")
        else:
            print(f"OK: {input_val} -> {result}")