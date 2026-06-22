def snake_to_camel(s: str) -> str:
    return s[0] + ''.join(word.capitalize() for word in s.split('_')[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('convert_this_string'))
    print(snake_to_camel('snake_case_to_camel'))
    print(snake_to_camel('alreadycamel'))
    print(snake_to_camel('single'))