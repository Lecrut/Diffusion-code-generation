def snake_to_camel(s: str) -> str:
    return ''.join(word.capitalize() for word in s.split('_'))

if __name__ == '__main__':
    print(snake_to_camel('hello_world'))
    print(snake_to_camel('foo_bar_baz'))
    print(snake_to_camel('single'))