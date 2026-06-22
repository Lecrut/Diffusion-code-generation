def to_camel_case(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        'user_name',
        'first_name',
        'last_name',
        'http_request_handler',
        'simple',
        'a_b_c_d_e_f_g',
        '_leading_underscore',
        'trailing_underscore_'
    ]
    for case in test_cases:
        result = to_camel_case(case)
        print(f"{case} -> {result}")