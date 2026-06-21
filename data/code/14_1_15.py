def check_unique_characters(s):
    assert isinstance(s, str), "Input must be a string"
    assert all(0 <= ord(c) <= 127 for c in s), "Input must contain only ASCII characters"
    
    if len(s) > 128:
        return False
    
    checker = 0
    for char in s:
        val = ord(char)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    result = check_unique_characters("abcdefg")
    print(result)
    result2 = check_unique_characters("hello")
    print(result2)
    result3 = check_unique_characters("")
    print(result3)