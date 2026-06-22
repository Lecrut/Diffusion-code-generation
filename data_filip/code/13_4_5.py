import re

def snake_to_camel(snake_str: str) -> str:
    parts = snake_str.split('_')
    if not parts:
        return ''
    result = parts[0]
    for part in parts[1:]:
        if part:
            result += part.capitalize()
    return result

if __name__ == '__main__':
    print(snake_to_camel('this_is_a_test_string'))