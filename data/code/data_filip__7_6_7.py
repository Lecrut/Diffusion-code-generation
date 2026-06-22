import re

def has_special_characters(text: str) -> bool:
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    samples = ["Hello World", "Hello! World", "No_special_chars", "Has#Symbol"]
    results = [has_special_characters(s) for s in samples]
    print(results)