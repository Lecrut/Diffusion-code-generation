def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        'hello_world',
        'snake_case_string',
        'alreadycamel',
        'two_words',
        'a_b_c_d_e',
        'with_numbers_123',
        'trailing_',
        '_leading',
        '__multiple_underscores__',
        'single'
    ]
    for case in test_cases:
        print(snake_to_camel(case))