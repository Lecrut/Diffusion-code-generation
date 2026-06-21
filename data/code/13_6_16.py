def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    if len(components) == 0:
        return ''
    first = components[0]
    rest = [component.capitalize() for component in components[1:]]
    return ''.join([first] + rest)

if __name__ == '__main__':
    sample_values = [
        'hello_world',
        'snake_case_string',
        'already_camel',
        'single',
        'multiple___underscores',
        '_leading_underscore',
        'trailing_underscore_'
    ]
    for sample in sample_values:
        result = snake_to_camel(sample)
        print(f"{sample} -> {result}")