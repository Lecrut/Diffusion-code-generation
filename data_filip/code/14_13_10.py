def are_characters_distinct(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            return False
        char_counts[char] = 1
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "aabbcc"
    result_1 = are_characters_distinct(test_string_1)
    result_2 = are_characters_distinct(test_string_2)
    print(result_1)
    print(result_2)