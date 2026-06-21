def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if components == ['']:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_a_test'))
    print(snake_to_camel('camel_case'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('single'))
    print(snake_to_camel(''))
    print(snake_to_camel('_leading'))
    print(snake_to_camel('trailing_'))
    print(snake_to_camel('multiple___underscores'))