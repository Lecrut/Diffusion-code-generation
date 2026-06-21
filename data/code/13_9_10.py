def to_camel_case(snake_str):
    if not snake_str:
        return snake_str
    parts = snake_str.split('_')
    if not parts[0]:
        parts = parts[1:]
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = ['hello_world', 'this_is_a_test', 'snake_case_conversion', '_leading_underscore', 'trailing_', '']
    for case in test_cases:
        print(to_camel_case(case))