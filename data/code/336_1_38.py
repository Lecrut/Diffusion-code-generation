def has_repeated_chars(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    test_cases = ["hello", "abcde", "", "a"]
    results = [has_repeated_chars(tc) for tc in test_cases]
    print(results)