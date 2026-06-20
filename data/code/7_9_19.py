import string

def contains_special_characters(s):
    special_characters = set(string.punctuation)
    return any(char in special_characters for char in s)

if __name__ == '__main__':
    print(contains_special_characters("Hello World"))
    print(contains_special_characters("Hello, World!"))
    print(contains_special_characters("Python3.9"))
    print(contains_special_characters("NoSpecialCharsHere"))
    print(contains_special_characters("Special@#$"))