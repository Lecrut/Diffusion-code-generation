import string

SPECIAL_CHARACTERS = set(string.punctuation)

def contains_special_chars(text: str) -> bool:
    text_set = set(text)
    return bool(text_set.intersection(SPECIAL_CHARACTERS))

if __name__ == '__main__':
    sample_strings = ["Hello World", "Hello! World", "No special chars"]
    for s in sample_strings:
        result = contains_special_chars(s)
        print(f"{s}: {result}")