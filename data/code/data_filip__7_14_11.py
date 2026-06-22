def has_special_chars(s, special_chars):
    return bool(set(s) & special_chars)

if __name__ == '__main__':
    test_string = "Hello, World!"
    special_chars = set("@#$%^&*()_+-=[]{}|;':\",./<>?")
    result = has_special_chars(test_string, special_chars)
    print(result)