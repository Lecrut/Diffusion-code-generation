def has_unique_chars_sorted(s):
    if len(s) != len(set(s)):
        return False
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    test1 = "abcdefg"
    test2 = "hello"
    test3 = ""
    test4 = "a"
    test5 = "aabbcc"

    print(has_unique_chars_sorted(test1))
    print(has_unique_chars_sorted(test2))
    print(has_unique_chars_sorted(test3))
    print(has_unique_chars_sorted(test4))
    print(has_unique_chars_sorted(test5))