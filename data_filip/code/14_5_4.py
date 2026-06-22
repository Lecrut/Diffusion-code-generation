def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "hello"
    print(has_unique_characters(test_string))
    test_string_2 = "world"
    print(has_unique_characters(test_string_2))