def snake_to_camel(snake_str):
    if not snake_str:
        return ''
    components = snake_str.split('_')
    return components[0] + ''.join(word.capitalize() for word in components[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_a_test'))
    print(snake_to_camel('single'))
    print(snake_to_camel(''))
    print(snake_to_camel('already_Camel'))