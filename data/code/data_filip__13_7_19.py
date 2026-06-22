import re

def to_camel_case(snake_str):
    parts = snake_str.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

def to_camel_case_regex(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ''
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part[0].upper() + part[1:]
    return result

if __name__ == '__main__':
    test_cases = [
        ('', ''),
        ('single', 'single'),
        ('hello_world', 'helloWorld'),
        ('this_is_a_snake_case_string', 'thisIsASnakeCaseString'),
        ('alreadyCamel', 'alreadyCamel'),
        ('_leading_underscore', 'leadingUnderscore'),
        ('trailing_underscore_', 'trailingUnderscore'),
        ('double__underscore', 'doubleUnderscore'),
    ]

    for snake, expected in test_cases:
        result = to_camel_case(snake)
        assert result == expected, f"Failed for {snake}: got {result}, expected {expected}"
        print(f"{snake} -> {result}")

    class CamelCaser:
        def __init__(self, input_string):
            self.input_string = input_string
        
        def to_camel(self):
            return to_camel_case(self.input_string)

    instance = CamelCaser('example_test_case')
    print(instance.to_camel())