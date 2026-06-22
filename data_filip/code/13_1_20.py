import re

def snake_to_camel(snake_str):
    parts = snake_str.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    result = snake_to_camel('this_is_a_test_string')
    print(result)