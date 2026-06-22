def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    filtered_parts = [part for part in parts if part]
    if not filtered_parts:
        return ''
    return filtered_parts[0] + ''.join(part.capitalize() for part in filtered_parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'foo_bar_baz',
        '_leading_underscore',
        'trailing_underscore_',
        '__double__underscores__',
        'alreadyCamel',
        'single',
        '_start_and_end_',
        'a_b_c',
        '___empty___parts___',
        '',
        '____',
        'no_underscores',
        'mixed_Case_snake',
    ]
    for sample in samples:
        result = snake_to_camel(sample)
        print(f'{sample!r} -> {result!r}')