def has_special_chars(text, special_chars):
    return bool(set(text) & special_chars)

if __name__ == '__main__':
    text1 = "hello world"
    text2 = "hello, world!"
    special = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")
    print(has_special_chars(text1, special))
    print(has_special_chars(text2, special))