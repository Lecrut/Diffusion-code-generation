def has_unique_chars(s):
    seen = set()
    for char in s:
        if char in seen:
            return False
        seen.add(char)
    return True

if __name__ == '__main__':
    result1 = has_unique_chars('abcde')
    result2 = has_unique_chars('hello')
    print(result1)
    print(result2)