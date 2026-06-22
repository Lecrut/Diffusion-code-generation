def all_characters_unique(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string = "abcdefg"
    result = all_characters_unique(test_string)
    print(result)
    test_string_duplicate = "programming"
    result_duplicate = all_characters_unique(test_string_duplicate)
    print(result_duplicate)