def has_unique_characters(s):
    counts = {}
    for char in s:
        counts[char] = counts.get(char, 0) + 1
    for count in counts.values():
        if count > 1:
            return False
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    result = has_unique_characters(test_string)
    print(result)