def snake_to_camel(s):
    if not s:
        return ''
    parts = s.split('_')
    if len(parts) == 1:
        return parts[0]
    return parts[0] + ''.join(part.capitalize() for part in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('this_is_a_test_string'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel(''))