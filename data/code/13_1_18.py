import re

def snake_to_camel(snake_str: str) -> str:
    return re.sub(r'_([a-z])', lambda m: m.group(1).upper(), snake_str)

if __name__ == '__main__':
    print(snake_to_camel('my_variable_name'))