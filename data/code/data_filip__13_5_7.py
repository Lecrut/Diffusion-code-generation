def snake_to_camel(s: str) -> str:
    return s[0] + ''.join(word.capitalize() for word in s[1:].split('_')) if '_' in s else s

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('foo_bar_baz'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('single'))