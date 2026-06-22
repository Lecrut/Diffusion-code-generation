def has_unique_characters(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "programming"
    print(has_unique_characters(test_string))
    test_string_2 = "abcdef"
    print(has_unique_characters(test_string_2))