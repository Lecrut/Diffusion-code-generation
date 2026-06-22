import string

SPECIAL_CHARS = set(string.punctuation)

def contains_special_char(text: str) -> bool:
    return bool(set(text) & SPECIAL_CHARS)

if __name__ == '__main__':
    sample_text = "Hello World!"
    result = contains_special_char(sample_text)
    print(result)