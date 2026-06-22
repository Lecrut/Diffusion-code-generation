def are_characters_distinct(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    result_1 = are_characters_distinct(test_string_1)
    result_2 = are_characters_distinct(test_string_2)
    print(result_1)
    print(result_2)