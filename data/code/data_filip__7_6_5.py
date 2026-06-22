import re

def has_special_characters(text: str) -> bool:
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample_text = "Hello, World!"
    result = has_special_characters(sample_text)
    print(result)