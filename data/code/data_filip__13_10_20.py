import re

def snake_to_camel(text: str) -> str:
    pattern = re.compile(r'_([a-zA-Z])')
    return pattern.sub(lambda match: match.group(1).upper(), text)

if __name__ == '__main__':
    result = snake_to_camel("hello_world_example")
    print(result)