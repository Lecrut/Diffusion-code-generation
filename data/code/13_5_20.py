import re

def snake_to_camel(text: str) -> str:
    components = text.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

if __name__ == '__main__':
    sample_input = "hello_world_example"
    print(snake_to_camel(sample_input))