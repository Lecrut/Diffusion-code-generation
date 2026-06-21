def has_unique_chars(s):
    if len(s) > 128:
        return False
    checker = 0
    for char in s:
        val = ord(char)
        if (checker & (1 << val)) > 0:
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    result1 = has_unique_chars("abcdefg")
    print(result1)
    result2 = has_unique_chars("hello")
    print(result2)
    assert has_unique_chars("abcdefg") is True
    assert has_unique_chars("hello") is False
    assert has_unique_chars("") is True
    assert has_unique_chars("a") is True
    assert has_unique_chars("ab") is True
    assert has_unique_chars("aa") is False
    assert has_unique_chars("abc...xyz") is False
    assert has_unique_chars("The quick brown fox") is False
    assert has_unique_chars("abcdefgHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-=[]{}|;':\",./<>?`~") is True
    print("All assertions passed.")