def has_repeated_chars(s: str) -> bool:
    return len(set(s)) != len(s)
if __name__ == '__main__':
    test_cases = ["hello", "abcdef", "", "a"]
    for tc in test_cases:
        result = has_repeated_chars(tc)
        print(f"'{tc}': {result}")