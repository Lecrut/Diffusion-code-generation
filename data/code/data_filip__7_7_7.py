import string

def has_special_characters(s):
    special_chars = set(string.punctuation)
    stripped = ''.join(c for c in s if c not in special_chars)
    return len(s) != len(stripped)

if __name__ == '__main__':
    print(has_special_characters("Hello World"))
    print(has_special_characters("Hello World!"))
    print(has_special_characters("NoSpecials123"))
    print(has_special_characters("Has@Symbol"))