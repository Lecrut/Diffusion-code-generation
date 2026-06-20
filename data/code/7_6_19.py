import re

def has_special_characters(text):
    pattern = re.compile(r'[^\w\s]')
    return bool(pattern.search(text))

if __name__ == '__main__':
    sample_texts = [
        "Hello World",
        "Hello! World",
        "Hello_World",
        "12345",
        "NoSpecials123"
    ]
    results = []
    for text in sample_texts:
        result = has_special_characters(text)
        results.append((text, result))
    print(results)