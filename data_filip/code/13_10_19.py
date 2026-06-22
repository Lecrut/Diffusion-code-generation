import re

def snake_to_camel(snake_str):
    if not snake_str:
        return snake_str
    components = re.split(r'_+', snake_str)
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    test_cases = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'single_word',
        '__leading_underscores__',
        'multiple___underscores',
        '',
        'a_b_c_d',
        'simple'
    ]
    for case in test_cases:
        print(f'{case!r} -> {snake_to_camel(case)!r}')