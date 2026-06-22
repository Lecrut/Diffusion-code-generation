def is_unique(s):
    if len(s) > 256:
        return False
    chars = set()
    for char in s:
        if char in chars:
            return False
        chars.add(char)
    return True

if __name__ == '__main__':
    test_string = "abcdefg"
    result = is_unique(test_string)
    print(result)