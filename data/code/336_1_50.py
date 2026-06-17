def has_repeated_chars(s: str) -> bool:
    return len(set(s)) != len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcdefg", "", "a"]
    for case in test_cases:
        result = has_repeated_chars(case)
        print(f"Input: '{case}', Output: {result}")