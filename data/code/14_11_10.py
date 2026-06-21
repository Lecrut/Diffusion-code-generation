def has_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    sample1 = "hello"
    sample2 = "world"
    sample3 = "abcdefg"
    sample4 = "aabbcc"
    sample5 = ""
    sample6 = "a"
    print(has_unique_chars(sample1))
    print(has_unique_chars(sample2))
    print(has_unique_chars(sample3))
    print(has_unique_chars(sample4))
    print(has_unique_chars(sample5))
    print(has_unique_chars(sample6))