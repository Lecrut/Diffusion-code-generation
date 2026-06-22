def is_unique(s):
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    print(is_unique(test_string))
    test_string_2 = "hello"
    print(is_unique(test_string_2))