def snake_to_camel(identifier):
    parts = identifier.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    samples = [
        'hello_world',
        'this_is_a_test',
        'alreadyCamel',
        'single',
        '_leading_underscore',
        'trailing_underscore_',
        '__double__',
        'a_b_c',
        '',
        'no_underscores'
    ]
    for sample in samples:
        print(snake_to_camel(sample))