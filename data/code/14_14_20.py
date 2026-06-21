def has_unique_chars_sorted(s):
    if not s:
        return True
    sorted_chars = sorted(s)
    for i in range(len(sorted_chars) - 1):
        if sorted_chars[i] == sorted_chars[i + 1]:
            return False
    return True

if __name__ == '__main__':
    print(has_unique_chars_sorted("abcdefg"))
    print(has_unique_chars_sorted("hello"))
    print(has_unique_chars_sorted("abcdefga"))
    print(has_unique_chars_sorted(""))
    print(has_unique_chars_sorted("a"))