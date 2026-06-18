def has_repeated_chars(s: str) -> bool:
    seen = set()
    for char in s:
        if char in seen:
            return True
        seen.add(char)
    return False
if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("aabbccdd", True),
        ("", False),
        ("aaa", True),
        ("abca", True)
    ]
    for input_str, expected in test_cases:
        result = has_repeated_chars(input_str)
        assert result == expected, f"Failed for '{input_str}': got {result}, expected {expected}"
    print("All tests passed.")