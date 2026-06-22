def to_camel_case(text):
    if not text:
        return text
    parts = text.split('_')
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_to_camel_case", "snakeCaseToCamelCase"),
        ("a", "a"),
        ("", ""),
        ("alreadyCamel", "alreadyCamel"),
        ("multiple___underscores", "multipleUnderscores"),
        ("single", "single"),
        ("this_is_a_test", "thisIsATest"),
    ]
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        status = "PASS" if result == expected else "FAIL"
        print(f"{input_val} -> {result} [{status}]")