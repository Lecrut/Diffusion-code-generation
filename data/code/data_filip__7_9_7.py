import string

def has_special_characters(s: str) -> bool:
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return True
    return False

if __name__ == '__main__':
    sample_strings = ["hello_world", "hello world", "hello!world", "12345"]
    for s in sample_strings:
        print(has_special_characters(s))