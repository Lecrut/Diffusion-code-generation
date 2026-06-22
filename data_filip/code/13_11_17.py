def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    sample_values = [
        'hello_world',
        'foo_bar_baz',
        'single',
        'a_b_c_d',
        '_leading_underscore',
        'trailing_underscore_',
        'multiple___underscores',
        ''
    ]
    for value in sample_values:
        result = snake_to_camel(value)
        print(result)