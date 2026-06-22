import string

def find_first_special_char(s):
    special_chars = set(string.punctuation)
    for char in s:
        if char in special_chars:
            return char
    return None

if __name__ == '__main__':
    print(find_first_special_char("Hello, World!"))
    print(find_first_special_char("NoSpecialCharsHere"))
    print(find_first_special_char("   "))
    print(find_first_special_char("123!456"))
    print(find_first_special_char("@Start"))