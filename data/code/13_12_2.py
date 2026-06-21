def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    test_cases = [
        'hello_world',
        'snake_case_to_camel_case',
        'alreadyCamel',
        'single',
        'with_numbers_123_test',
        '__leading_underscores',
        'trailing_underscores__',
        '',
        '_starts_with_underscore'
    ]
    for test in test_cases:
        print(f"{test} -> {snake_to_camel(test)}")