def reverse_string(s: str) -> str:
    """Reverse a string character by character."""
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate the reversal capability
    test_cases = ["Hello, World!", "Python", "", "A"]
    for case in test_cases:
        print(f"Original: {case!r} -> Reversed: {reverse_string(case)!r}")