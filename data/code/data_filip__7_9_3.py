import string

def has_special_characters(s: str) -> bool:
    return any(c in string.punctuation for c in s)

if __name__ == '__main__':
    print(has_special_characters("hello"))
    print(has_special_characters("hello!"))
    print(has_special_characters(""))
    print(has_special_characters("no special"))
    print(has_special_characters("@#$%"))