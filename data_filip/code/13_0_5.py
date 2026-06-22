def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'single',
        'with__double__underscores',
        '_leading',
        'trailing_',
        '',
        'a_b_c'
    ]
    for sample in samples:
        print(f"snake_to_camel('{sample}') -> '{snake_to_camel(sample)}'")