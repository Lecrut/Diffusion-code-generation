def has_unique_characters(s):
    seen_chars = set()
    for char in s:
        if char in seen_chars:
            return False
        seen_chars.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    print(has_unique_characters(test_string_1))
    print(has_unique_characters(test_string_2))