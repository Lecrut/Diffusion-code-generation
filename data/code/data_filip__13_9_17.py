def snake_to_camel(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_values = [
        "hello_world",
        "snake_case_string",
        "a_b_c_d",
        "single",
        "_leading_underscore",
        "trailing_underscore_",
        "multiple___underscores",
        ""
    ]
    for val in sample_values:
        print(snake_to_camel(val))