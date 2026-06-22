import re

def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = ['hello_world', 'snake_case_to_camel_case', 'single', 'alreadyCamel', 'with_numbers_123']
    for case in test_cases:
        print(snake_to_camel(case))