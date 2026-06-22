def snake_to_camel(s):
    if not s:
        return ''
    parts = s.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('snake_case_to_camel'))
    print(snake_to_camel('simple'))
    print(snake_to_camel('a_b_c_d'))
    print(snake_to_camel('_leading_underscore'))
    print(snake_to_camel('trailing_underscore_'))