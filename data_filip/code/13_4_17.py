import re
import functools

def snake_to_camel(snake_str: str) -> str:
    if not snake_str:
        return ''
    parts = snake_str.split('_')
    return parts[0] + ''.join((word.capitalize() for word in parts[1:] if word))
if __name__ == '__main__':
    result = snake_to_camel('hello_world_example')
    print(result)