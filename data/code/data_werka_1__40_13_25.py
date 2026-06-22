import string

def get_first_alphabetic_character(s):
    ALPHABETIC_CHARS = set(string.ascii_letters)
    for char in s:
        if char in ALPHABETIC_CHARS:
            return char
    return None

if __name__ == '__main__':
    sample_strings = ["!@#abc", "123456", "no leading numbers", " ", "", "Python3.8"]
    results = [get_first_alphabetic_character(s) for s in sample_strings]
    print(results)