def has_unique_chars(s):
    visited = set()
    for char in s:
        if char in visited:
            return False
        visited.add(char)
    return True

if __name__ == '__main__':
    sample_strings = [
        "abcdef",
        "hello",
        "world",
        "abcdefg",
        "aabbcc",
        "",
        "a"
    ]
    for sample in sample_strings:
        result = has_unique_chars(sample)
        print(result)