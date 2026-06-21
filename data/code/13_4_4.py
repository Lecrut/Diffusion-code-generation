def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'simple',
        'with__double__underscores',
        'leading_underscore_case',
        'trailing_underscore_case_',
        'a_b_c_d_e'
    ]
    for test in test_cases:
        print(f"{test} -> {snake_to_camel(test)}")