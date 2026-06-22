def is_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    print(is_unique_chars('abcdef'))
    print(is_unique_chars('hello'))
    print(is_unique_chars(''))
    print(is_unique_chars('a'))