def contains_unique_characters(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    result_1 = contains_unique_characters(test_string_1)
    result_2 = contains_unique_characters(test_string_2)
    print(result_1)
    print(result_2)