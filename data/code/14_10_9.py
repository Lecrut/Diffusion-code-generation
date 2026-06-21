def has_unique_characters(s):
    return len(s) == len(set(s))

if __name__ == '__main__':
    test_cases = [
        "hello",
        "world",
        "abcdef",
        "aabbcc",
        "",
        "unique!",
    ]
    for test in test_cases:
        print(has_unique_characters(test))