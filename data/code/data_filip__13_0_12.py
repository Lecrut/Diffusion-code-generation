def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = [comp.capitalize() for comp in components[1:]]
    return first + ''.join(rest)
if __name__ == '__main__':
    test_cases = ['hello_world', 'this_is_a_test', 'alreadycamel', 'single', '_leading', 'trailing_', '__double__underscores__', 'a_b_c_d_e']
    for test in test_cases:
        result = snake_to_camel(test)
        print(f'{test} -> {result}')