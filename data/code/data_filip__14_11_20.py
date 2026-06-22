def has_unique_characters(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    test_cases = [
        "abcdefg",
        "hello",
        "python",
        "aab",
        "",
        "a"
    ]
    for test in test_cases:
        print(has_unique_characters(test))