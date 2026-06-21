def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "this_is_a_test_string",
        "single",
        "multiple___underscores",
        "trailing_",
        "_leading"
    ]
    for case in test_cases:
        result = snake_to_camel(case)
        print(f"{case} -> {result}")