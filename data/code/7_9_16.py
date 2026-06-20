import string

def contains_special_char(s: str) -> bool:
    return any(c in string.punctuation for c in s)

if __name__ == '__main__':
    print(contains_special_char("hello world"))
    print(contains_special_char("hello, world!"))
    print(contains_special_char("no_special_chars"))
    print(contains_special_char("@#$%"))