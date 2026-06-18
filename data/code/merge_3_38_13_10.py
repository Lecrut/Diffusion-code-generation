def has_repeated_letters(s: str) -> bool:
    """Check if a string contains any repeated letters."""
    return len(set(s)) != len({c for c in s if c.isalpha()})

if __name__ == '__main__':
    # Sample test cases without user input
    samples = [
        ("hello", True),       # 'l' and 'o' repeat
        ("abcdef", False),     # all unique
        ("aA12#", True),       # case-insensitive letter repetition ('a', 'A') is not detected by default set logic, let's adjust for case-sensitivity if needed. The task says "letters". Usually implies case-sensitive unless specified otherwise. Let's stick to strict character equality first as per standard interpretation.
        ("hello", True),       # Re-run with clear example
    ]

    print("Testing has_repeated_letters:\n")
    for test_str, expected in samples:
        result = has_repeated_letters(test_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"'{test_str}' -> {result} (Expected: {expected}) [{status}]")