def has_unique_characters(s):
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if checker & (1 << val):
            return False
        checker |= 1 << val
    return True

if __name__ == '__main__':
    test_string_1 = "hello"
    test_string_2 = "world"
    test_string_3 = "abc"
    result_1 = has_unique_characters(test_string_1)
    result_2 = has_unique_characters(test_string_2)
    result_3 = has_unique_characters(test_string_3)
    print(result_1)
    print(result_2)
    print(result_3)