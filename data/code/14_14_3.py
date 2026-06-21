def has_unique_chars(s):
    if len(s) > 256:
        return False
    sorted_s = sorted(s)
    for i in range(1, len(sorted_s)):
        if sorted_s[i] == sorted_s[i - 1]:
            return False
    return True

if __name__ == '__main__':
    print(has_unique_chars("abcde"))
    print(has_unique_chars("aabbcc"))
    print(has_unique_chars(""))