import re

def snake_to_camel(s: str) -> str:
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), s)

if __name__ == '__main__':
    print(snake_to_camel('hello_world_example'))