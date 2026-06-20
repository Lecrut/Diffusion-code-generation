import re

def has_special_characters(text: str) -> bool:
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    sample_text = "Hello World! 123"
    result = has_special_characters(sample_text)
    print(result)