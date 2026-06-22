def has_unique_chars(s):
    if len(s) > 128:
        return False
    checker = 0
    for c in s:
        val = ord(c)
        if checker & (1 << val):
            return False
        checker |= (1 << val)
    return True

assert has_unique_chars("") == True
assert has_unique_chars("abc") == True
assert has_unique_chars("aab") == False
assert has_unique_chars("abcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefgabcdefg!@#$%^&*()_+-=[]{}|;':,./<>?~`0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ") == False

if __name__ == '__main__':
    print(has_unique_chars("hello"))
    print(has_unique_chars("world"))
    print(has_unique_chars("aabbcc"))
    print(has_unique_chars("unique"))
    print(has_unique_chars(""))
    print(has_unique_chars("abcdef"))