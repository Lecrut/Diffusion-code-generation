def to_camel_case(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    print(to_camel_case('my_variable_name'))
    print(to_camel_case('alreadyCamel'))
    print(to_camel_case('simple'))
    print(to_camel_case('with_many_words'))