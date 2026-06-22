def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False
    char_set = [False] * 128
    for char in s:
        index = ord(char)
        if index >= 128:
            return False
        if char_set[index]:
            return False
        char_set[index] = True
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    print(is_unique(test_string))
    test_string_dup = "hello"
    print(is_unique(test_string_dup))