def all_unique_characters(s):
    seen = {}
    for char in s:
        if char in seen:
            return False
        seen[char] = True
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "aabbcc"
    print(all_unique_characters(test_string_1))
    print(all_unique_characters(test_string_2))