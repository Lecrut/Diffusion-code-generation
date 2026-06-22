def is_unique(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    test_string_1 = "abcdef"
    test_string_2 = "programming"
    print(is_unique(test_string_1))
    print(is_unique(test_string_2))