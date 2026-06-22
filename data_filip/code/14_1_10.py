def is_unique_chars(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if val >= 128:
            return False
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    sample1 = "abcdef"
    sample2 = "aabbcc"
    sample3 = "Hello"
    result1 = is_unique_chars(sample1)
    result2 = is_unique_chars(sample2)
    result3 = is_unique_chars(sample3)
    assert result1 == True
    assert result2 == False
    assert result3 == False
    print(result1)
    print(result2)
    print(result3)