import re
import sys

def convert_to_camel_case(text):
    def replace(match):
        word = match.group(1)
        return word[0].upper() + word[1:].lower() if word else ""

    return re.sub(r'_([a-zA-Z0-9])', replace, text).lower() if text else text

def convert_to_camel_case_standard(text):
    parts = text.split('_')
    return parts[0] + ''.join(word.capitalize() for word in parts[1:]) if parts else text

def snake_to_camel(text):
    return convert_to_camel_case_standard(text)

if __name__ == '__main__':
    samples = ["hello_world", "snake_case_to_camel", "simple", "", "alreadyCamel", "multi_part_value_test"]
    for s in samples:
        print(snake_to_camel(s))