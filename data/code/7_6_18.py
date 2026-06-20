import re

def has_special_characters(text: str) -> bool:
    pattern = re.compile(r'[^a-zA-Z0-9\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    result1 = has_special_characters("Hello, World!")
    print(result1)
    result2 = has_special_characters("Hello World")
    print(result2)
    result3 = has_special_characters("12345")
    print(result3)