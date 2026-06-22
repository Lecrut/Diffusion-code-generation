import re

def find_first_special_char(text: str):
    special_pattern = re.compile(r'[^a-zA-Z0-9\s]')
    match = special_pattern.search(text)
    if match:
        return match.group(0)
    return None

if __name__ == '__main__':
    result1 = find_first_special_char("Hello World")
    print(result1)
    result2 = find_first_special_char("Hello, World!")
    print(result2)
    result3 = find_first_special_char("12345")
    print(result3)