def has_repeated_chars(s: str) -> bool:
    return len(set(s)) != len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcde", "aabbcc", "unique"]
    for case in test_cases:
        print(f"'{case}': {has_repeated_chars(case)}")