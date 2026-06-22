def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = [comp.capitalize() for comp in components[1:]]
    return ''.join([first] + rest)

if __name__ == '__main__':
    sample1 = 'hello_world'
    sample2 = 'convert_this_string'
    sample3 = 'alreadyCamel'
    print(snake_to_camel(sample1))
    print(snake_to_camel(sample2))
    print(snake_to_camel(sample3))