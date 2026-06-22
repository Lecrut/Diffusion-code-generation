def is_unique(s):
    if len(s) > 128:
        return False
    char_set = set()
    for char in s:
        if char in char_set:
            return False
        char_set.add(char)
    return True

if __name__ == '__main__':
    sample_string = "abcdefg"
    result = is_unique(sample_string)
    print(result)