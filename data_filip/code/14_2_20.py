def are_characters_unique(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "abcdefg"
    result = are_characters_unique(test_string)
    print(result)
    test_string_duplicate = "hello"
    result_duplicate = are_characters_unique(test_string_duplicate)
    print(result_duplicate)