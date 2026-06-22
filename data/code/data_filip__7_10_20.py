import re

def has_special_characters(text: str) -> bool:
    return bool(re.search(r'[^a-zA-Z0-9]', text))

if __name__ == '__main__':
    sample1 = "Hello World"
    sample2 = "Hello World!"
    sample3 = "12345"
    sample4 = "User@Name"

    print(has_special_characters(sample1))
    print(has_special_characters(sample2))
    print(has_special_characters(sample3))
    print(has_special_characters(sample4))