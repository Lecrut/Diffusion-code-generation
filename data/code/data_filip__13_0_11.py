def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    if not components:
        return ''
    first = components[0]
    rest = [component.title() for component in components[1:]]
    return ''.join([first] + rest)

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_to_camel_case'))
    print(snake_to_camel('single'))
    print(snake_to_camel(''))
    print(snake_to_camel('alreadyCamel'))