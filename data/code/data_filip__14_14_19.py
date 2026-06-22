def has_unique_chars(s):
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(1, len(sorted_chars)):
        if sorted_chars[i] == sorted_chars[i - 1]:
            return False
    return True

if __name__ == '__main__':
    print(has_unique_chars("abcdef"))
    print(has_unique_chars("hello"))
    print(has_unique_chars(""))
    print(has_unique_chars("a"))
    print(has_unique_chars("aab"))