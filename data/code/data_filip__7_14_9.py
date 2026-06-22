SPECIAL_CHARS = set("!@#$%^&*()_+-=[]{}|;:,.<>?/~`")

def has_special_characters(s):
    return bool(set(s) & SPECIAL_CHARS)

if __name__ == '__main__':
    print(has_special_characters("hello world"))
    print(has_special_characters("hello! world"))