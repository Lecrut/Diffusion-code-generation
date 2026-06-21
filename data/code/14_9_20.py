def has_all_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "aabbcc"
    test_string_3 = "Hello"
    print(has_all_unique_characters(test_string_1))
    print(has_all_unique_characters(test_string_2))
    print(has_all_unique_characters(test_string_3))