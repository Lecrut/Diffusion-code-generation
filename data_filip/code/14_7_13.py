def is_unique(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "aabbcc"
    print(is_unique(test_string_1))
    print(is_unique(test_string_2))