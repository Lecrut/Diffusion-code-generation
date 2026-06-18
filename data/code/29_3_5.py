def reverse_string(s: str) -> str:
    """Reverse a string character by character."""
    return s[::-1]

if __name__ == '__main__':
    test_cases = ["Hello, World!", "Python", "!olleH"]
    for case in test_cases:
        print(f"Original: {case} -> Reversed: {reverse_string(case)}")