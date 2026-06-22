def has_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    sample1 = "abcdefg"
    sample2 = "hello"
    sample3 = ""
    sample4 = "a"
    sample5 = "abca"

    print(has_unique_chars(sample1))
    print(has_unique_chars(sample2))
    print(has_unique_chars(sample3))
    print(has_unique_chars(sample4))
    print(has_unique_chars(sample5))