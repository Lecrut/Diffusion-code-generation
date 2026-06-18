def is_palindrome(s: str) -> bool:
    """Check if a string is a palindrome."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input.
    test_strings = [
        "racecar",
        "hello",
        "A man a plan a canal Panama"  # This one is not strictly palindrome due to spaces and case, handled by simple check above.
    ]

    for text in test_strings:
        result = is_palindrome(text)
        if result:
            print(f"'{text}' is a palindrome.")
        else:
            print(f"'{text}' is NOT a palindrome.")