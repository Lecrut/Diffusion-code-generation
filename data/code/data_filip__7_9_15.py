import string

def has_special_characters(text: str) -> bool:
    return any(c in string.punctuation for c in text)

if __name__ == '__main__':
    sample_strings = ["hello_world", "hello world", "Hello!@#", "no_specials"]
    for s in sample_strings:
        print(has_special_characters(s))