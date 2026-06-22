def has_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    print(has_unique_chars("abcdef"))
    print(has_unique_chars("hello"))
    print(has_unique_chars(""))
    print(has_unique_chars("a"))
    print(has_unique_chars("abca"))