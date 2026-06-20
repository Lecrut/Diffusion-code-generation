import re

def contains_special_characters(text: str) -> bool:
    pattern = r'[^a-zA-Z0-9]'
    return bool(re.search(pattern, text))

if __name__ == '__main__':
    samples = ['hello world', 'hello@world', '12345', 'Test!123']
    for sample in samples:
        result = contains_special_characters(sample)
        print(result)