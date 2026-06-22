import re

def snake_to_camel(snake_str):
    parts = re.split(r'_+', snake_str)
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    print(snake_to_camel('hello_world_name'))
    print(snake_to_camel('alreadyCamel'))
    print(snake_to_camel('multiple___underscores'))
    print(snake_to_camel('single'))