import re

def snake_to_camel(snake_str):
    components = re.sub(r'^_+', '', snake_str).split('_')
    if not components:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_inputs = [
        'hello_world',
        'snake_case_string',
        '_leading_underscore',
        'trailing_underscore_',
        'multiple___underscores',
        'alreadyCamel',
        'simple',
        '_starts_with_underscore',
        'ends_with_underscore_',
        '__double__underscores__',
    ]
    for s in sample_inputs:
        print(snake_to_camel(s))