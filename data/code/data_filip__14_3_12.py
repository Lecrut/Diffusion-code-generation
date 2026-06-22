def has_unique_chars(s):
    if s is None:
        return True
    char_list = list(s)
    length = len(char_list)
    if length < 2:
        return True
    for i in range(length - 1):
        for j in range(i + 1, length):
            if char_list[i] == char_list[j]:
                return False
    return True

if __name__ == '__main__':
    test_string_1 = "programming"
    test_string_2 = "abcdefg"
    print(has_unique_chars(test_string_1))
    print(has_unique_chars(test_string_2))