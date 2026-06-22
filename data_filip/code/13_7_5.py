def snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    result1 = snake_to_camel('hello_world')
    result2 = snake_to_camel('this_is_a_test')
    result3 = snake_to_camel('alreadyCamel')
    print(result1)
    print(result2)
    print(result3)