def has_repeated_chars(text: str) -> bool:
    return len(set(text)) != len(text)
if __name__ == '__main__':
    test_cases = ["hello", "abcdefg", "aabbcc"]
    for case in test_cases:
        print(has_repeated_chars(case))