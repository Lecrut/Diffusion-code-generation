def to_camel_case(snake_str):
    if not snake_str:
        return ""
    components = snake_str.split('_')
    return components[0] + ''.join(x.capitalize() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        "snake_case_identifier",
        "convert_this_string",
        "alreadyCamelCase",
        "single",
        "multiple___underscores__here",
        "a_b_c_d_e_f"
    ]
    for case in test_cases:
        result = to_camel_case(case)
        print(f"{case} -> {result}")