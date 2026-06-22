def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = [component.capitalize() for component in components[1:]]
    return first + ''.join(rest)

if __name__ == '__main__':
    sample1 = 'hello_world'
    sample2 = 'this_is_a_test'
    sample3 = 'alreadyCamel'
    sample4 = ''
    sample5 = 'single'

    print(snake_to_camel(sample1))
    print(snake_to_camel(sample2))
    print(snake_to_camel(sample3))
    print(snake_to_camel(sample4))
    print(snake_to_camel(sample5))