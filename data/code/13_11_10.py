def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    if len(parts) == 1:
        return parts[0]
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "snake_case_identifier",
        "simple",
        "alreadyCamel",
        "multiple___underscores",
        "_leading",
        "trailing_",
        "__both__",
        "a_b_c",
        ""
    ]
    for tc in test_cases:
        print(snake_to_camel(tc))