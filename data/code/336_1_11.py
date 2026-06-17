def has_repeated_chars(s: str) -> bool:
    return len(set(s)) != len(s)
if __name__ == '__main__':
    test_cases = [
        ("hello", True),
        ("abcdef", False),
        ("aabbccdd", True),
        ("", False),
        ("aaaa", True),
        ("1234567890", False)
    ]
    for input_str, expected in test_cases:
        result = has_repeated_chars(input_str)
        assert result == expected, f"Failed for '{input_str}': got {result}, expected {expected}"