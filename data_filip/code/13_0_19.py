def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ''
    components = snake_str.split('_')
    first_component = components[0].lower()
    rest_components = [comp.capitalize() for comp in components[1:]]
    return first_component + ''.join(rest_components)
if __name__ == '__main__':
    test_cases = ['hello_world', 'snake_case_to_camel', 'alreadyCamel', 'single', '_leading_underscore', 'trailing_underscore_', 'multiple___underscores', 'with1numbers2', '', 'a_b_c_d_e']
    for test in test_cases:
        result = snake_to_camel(test)
        print(f"snake_to_camel('{test}') = '{result}'")