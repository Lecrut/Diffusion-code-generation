def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    test_string_3 = ""
    print(has_unique_characters(test_string_1))
    print(has_unique_characters(test_string_2))
    print(has_unique_characters(test_string_3))