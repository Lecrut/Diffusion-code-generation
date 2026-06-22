def snake_to_camel(snake_str):
    components = snake_str.split('_')
    if not components:
        return ''
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_to_camel'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('simple'))
    print(snake_to_camel(''))
    print(snake_to_camel('trailing_'))