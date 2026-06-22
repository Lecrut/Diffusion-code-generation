import re
import string

def convert_snake_to_camel(text: str) -> str:
    parts = text.split('_')
    if not parts:
        return ''
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])

if __name__ == '__main__':
    result = convert_snake_to_camel('this_is_a_test_string')
    print(result)