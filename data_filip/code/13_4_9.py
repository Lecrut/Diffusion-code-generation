import re

def convert_snake_to_camel(snake_str: str) -> str:
    components = snake_str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    result = convert_snake_to_camel("hello_world")
    print(result)