SPECIAL_CHARACTERS = set('!@#$%^&*()_+-=[]{}|;:,.<>?/~`')

def has_special_chars(text):
    return bool(set(text) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    print(has_special_chars("hello"))
    print(has_special_chars("hello!"))
    print(has_special_chars("world#123"))
    print(has_special_chars(""))