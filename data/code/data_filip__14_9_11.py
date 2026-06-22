def has_unique_characters(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "hello"
    result_1 = has_unique_characters(test_string_1)
    result_2 = has_unique_characters(test_string_2)
    print(result_1)
    print(result_2)