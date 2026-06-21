def has_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    test_strings = [
        "hello",
        "world",
        "abcdefg",
        "aabbcc",
        "python3",
        "",
        "12345",
        "12321"
    ]
    for test_str in test_strings:
        result = has_unique_chars(test_str)
        print(f"has_unique_chars({repr(test_str)}) = {result}")