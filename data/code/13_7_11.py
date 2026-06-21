def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "simple_snake_case",
        "already_camel",
        "multiple___underscores",
        "a_b_c_d_e",
        "single",
        "two_words",
        "leading_underscore",
        "trailing_underscore_",
        "UPPER_CASE"
    ]
    for test in test_cases:
        print(snake_to_camel(test))