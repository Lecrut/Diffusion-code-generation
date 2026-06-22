import re

def contains_special_characters(text: str) -> bool:
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    print(contains_special_characters("Hello World!"))
    print(contains_special_characters("Hello World"))
    print(contains_special_characters("12345"))
    print(contains_special_characters("   "))
    print(contains_special_characters(""))