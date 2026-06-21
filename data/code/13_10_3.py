import re

def snake_to_camel(snake_str):
    components = re.split(r'_+', snake_str)
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_values = [
        'hello_world',
        'this_is_snake_case',
        'alreadyCamel',
        'single',
        '__leading__underscores__',
        'trailing___underscores',
        'multiple___consecutive_underscores',
        'with_numbers_123_and_more',
        'UPPER_CASE_INPUT',
        'mixed_Case_Snake_input'
    ]
    for sample in sample_values:
        result = snake_to_camel(sample)
        print(result)