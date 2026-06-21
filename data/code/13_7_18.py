def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_to_camel_case", "snakeCaseToCamelCase"),
        ("single", "single"),
        ("multiple_underscore_separators_here", "multipleUnderscoreSeparatorsHere"),
        ("", ""),
        ("alreadyCamelCase", "alreadyCamelCase"),
    ]
    for input_val, expected in test_cases:
        result = to_camel_case(input_val)
        print(f"{input_val} -> {result}")