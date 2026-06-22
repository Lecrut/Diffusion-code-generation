def is_unique(s: str) -> bool:
    if len(s) > 128:
        return False
    char_set = [False] * 128
    for char in s:
        val = ord(char)
        if char_set[val]:
            return False
        char_set[val] = True
    return True

if __name__ == '__main__':
    test_string = "programming"
    result = is_unique(test_string)
    print(result)