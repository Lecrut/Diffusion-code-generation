import string

def contains_special_chars(text: str) -> bool:
    special_chars = set(string.punctuation)
    for char in text:
        if char in special_chars:
            return True
    return False

if __name__ == '__main__':
    print(contains_special_chars("Hello World"))
    print(contains_special_chars("Hello, World!"))