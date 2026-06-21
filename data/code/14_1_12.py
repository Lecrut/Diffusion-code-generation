def has_unique_chars(s):
    checker = 0
    for char in s:
        val = ord(char)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True

if __name__ == '__main__':
    assert has_unique_chars('abc') == True
    assert has_unique_chars('aabb') == False
    assert has_unique_chars('') == True
    assert has_unique_chars('ab!c') == True
    assert has_unique_chars('ab!c!') == False
    print(has_unique_chars('abc'))
    print(has_unique_chars('aabb'))