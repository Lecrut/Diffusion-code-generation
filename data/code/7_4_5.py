import string

def first_special_char(s):
    special_characters = set(string.punctuation + string.whitespace)
    for char in s:
        if char in special_characters:
            return char
    return None

if __name__ == '__main__':
    print(first_special_char("hello world"))
    print(first_special_char("Hello, World!"))
    print(first_special_char("NoSpecialCharsHere"))
    print(first_special_char("   Leading spaces"))
    print(first_special_char("Trailing punctuation!"))