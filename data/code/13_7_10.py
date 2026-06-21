def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        ('hello_world', 'helloWorld'),
        ('this_is_snake_case', 'thisIsSnakeCase'),
        ('alreadyCamel', 'alreadyCamel'),
        ('single_word', 'singleWord'),
        ('with__double__underscores', 'withDoubleUnderscores'),
        ('', ''),
        ('_', ''),
        ('_leading', 'Leading'),
        ('trailing_', 'trailing'),
        ('a_b_c_d', 'aBCD')
    ]
    for input_str, expected in test_cases:
        result = snake_to_camel(input_str)
        print(f"snake_to_camel('{input_str}') = '{result}' (expected: '{expected}') -> {'PASS' if result == expected else 'FAIL'}")