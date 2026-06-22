def all_distinct_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "programming"
    result_1 = all_distinct_chars(test_string_1)
    result_2 = all_distinct_chars(test_string_2)
    print(result_1)
    print(result_2)