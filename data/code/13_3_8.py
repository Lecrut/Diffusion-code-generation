def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    if not parts:
        return ''
    first = parts[0]
    rest = [part.capitalize() for part in parts[1:] if part]
    return ''.join([first] + rest)

if __name__ == '__main__':
    samples = [
        'hello_world',
        'snake_case_string',
        'alreadyCamel',
        'single',
        'multiple___underscores',
        '_leading',
        'trailing_',
        '',
        'a_b_c_d_e'
    ]
    for sample in samples:
        print(snake_to_camel(sample))