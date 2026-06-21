def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if len(components) == 1:
        return components[0]
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        ("hello_world", "helloWorld"),
        ("snake_case_string", "snakeCaseString"),
        ("alreadyCamel", "alreadyCamel"),
        ("a_b_c_d", "aBCD"),
        ("_leading", "leading"),
        ("trailing_", "trailing"),
        ("__multiple", "multiple"),
        ("no_underscore", "noUnderscore"),
        ("single", "single"),
        ("a", "a"),
        ("hello___world", "helloWorld"),
        ("_start", "start"),
        ("end_", "end"),
    ]
    
    for snake_input, expected in test_cases:
        result = snake_to_camel(snake_input)
        print(f"snake_to_camel('{snake_input}') = '{result}', expected '{expected}', match={result == expected}")