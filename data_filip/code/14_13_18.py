def are_all_characters_distinct(s: str) -> bool:
    char_count = {}
    for char in s:
        if char in char_count:
            return False
        char_count[char] = 1
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    test_string_3 = ""
    print(are_all_characters_distinct(test_string_1))
    print(are_all_characters_distinct(test_string_2))
    print(are_all_characters_distinct(test_string_3))