SPECIAL_CHARACTERS = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")

def has_special_chars(s):
    return bool(set(s) & SPECIAL_CHARACTERS)

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "hello!"
    print(has_special_chars(sample1))
    print(has_special_chars(sample2))