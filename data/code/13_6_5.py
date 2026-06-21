import re

def snake_to_camel(text: str) -> str:
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    result = snake_to_camel('hello_world')
    print(result)