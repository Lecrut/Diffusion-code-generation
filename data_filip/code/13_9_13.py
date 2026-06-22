def to_camel_case(snake_str: str) -> str:
    if not snake_str:
        return ""
    parts = snake_str.split('_')
    first = parts[0]
    remaining = [word.capitalize() for word in parts[1:]]
    return first + ''.join(remaining)

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "user_profile_data",
        "this_is_a_test_string",
        "single",
        "alreadyCamelCase",
        "multiple___underscores",
        "_leading_underscore",
        "trailing_underscore_",
    ]
    for case in test_cases:
        print(to_camel_case(case))