def has_distinct_characters(s):
    char_counts = {}
    for char in s:
        char_counts[char] = char_counts.get(char, 0) + 1
    for count in char_counts.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = has_distinct_characters(test_string)
    print(result)