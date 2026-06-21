def snake_to_camel(snake_str):
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_inputs = [
        'hello_world',
        'foo_bar_baz',
        'single',
        'already_Camel',
        'trailing_underscore_',
        '__leading'
    ]
    for s in sample_inputs:
        print(snake_to_camel(s))