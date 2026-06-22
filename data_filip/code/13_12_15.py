def snake_to_camel(snake_str):
    if not snake_str:
        return ''
    parts = snake_str.split('_')
    if not parts:
        return ''
    result = parts[0] + ''.join(word.capitalize() for word in parts[1:])
    return result

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('convert_this_string'))
    print(snake_to_camel('single'))
    print(snake_to_camel('with___multiple___underscores'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel(''))