def are_characters_unique(s):
    return len(set(s)) == len(s)

if __name__ == '__main__':
    test_string = "abcdef"
    print(are_characters_unique(test_string))
    test_string_dup = "hello"
    print(are_characters_unique(test_string_dup))