def has_all_distinct_chars(s):
    char_count = {}
    for char in s:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    for count in char_count.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = has_all_distinct_chars(test_string)
    print(result)