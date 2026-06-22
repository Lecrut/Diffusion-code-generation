def has_unique_characters(s):
    char_counts = {}
    for char in s:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    for count in char_counts.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdef"
    result = has_unique_characters(test_string)
    print(result)