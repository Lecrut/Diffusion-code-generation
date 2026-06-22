def has_duplicate_chars(s: str) -> bool:
    if not s:
        return False
    checker = 0
    for char in s:
        val = ord(char) - ord('a')
        if val < 0 or val > 25:
            raise ValueError("Input must contain only lowercase ASCII letters")
        if (checker & (1 << val)) != 0:
            return True
        checker |= (1 << val)
    return False

if __name__ == '__main__':
    test_string_1 = "programming"
    test_string_2 = "abcdef"
    test_string_3 = "hello"
    test_string_4 = "world"
    result_1 = has_duplicate_chars(test_string_1)
    result_2 = has_duplicate_chars(test_string_2)
    result_3 = has_duplicate_chars(test_string_3)
    result_4 = has_duplicate_chars(test_string_4)
    print(result_1)
    print(result_2)
    print(result_3)
    print(result_4)