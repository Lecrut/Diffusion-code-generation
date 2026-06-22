def has_special_characters(s):
    special_symbols = set("!@#$%^&*()_+-=[]{}|;':\",./<>?")
    return bool(special_symbols & set(s))

if __name__ == '__main__':
    test_string_1 = "HelloWorld"
    test_string_2 = "Hello@World!"
    test_string_3 = "SpecialChars#Here$%"
    print(has_special_characters(test_string_1))
    print(has_special_characters(test_string_2))
    print(has_special_characters(test_string_3))