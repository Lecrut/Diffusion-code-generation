def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_values = [
        'hello_world',
        'foo_bar_baz',
        'alreadyCamel',
        'single',
        'with__double__underscores',
        'leading_trailing_',
        '_starts_with_underscore',
        'ends_with_underscore_'
    ]
    for value in sample_values:
        result = snake_to_camel(value)
        print(result)