import re

def snake_to_camel(name: str) -> str:
    parts = name.split('_')
    if not parts:
        return ''
    result = [parts[0]]
    for part in parts[1:]:
        if part:
            result.append(part.capitalize())
    return ''.join(result)

if __name__ == '__main__':
    print(snake_to_camel("hello_world"))
    print(snake_to_camel("foo_bar_baz"))
    print(snake_to_camel("simple"))
    print(snake_to_camel("_leading_underscore"))
    print(snake_to_camel("trailing_underscore_"))
    print(snake_to_camel("multiple___underscores"))