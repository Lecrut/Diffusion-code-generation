def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "hello_world",
        "snake_case_to_camel_case",
        "single",
        "a_b_c_d_e",
        "alreadyCamelCase_should_remain_unchanged_if_no_underscores"
    ]
    for case in test_cases:
        print(snake_to_camel(case))