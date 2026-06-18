def is_palindrome_optimized(s: str) -> bool:
    """Check if a string is a palindrome by comparing original with reversed version."""
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input, network access, or file dependency.
    test_strings = [
        "racecar",
        "hello",
        "A man a plan a canal Panama",  # Case-insensitive check not requested but common; here case-sensitive as per task logic unless specified otherwise. 
                                        # Task says 'original string with its reversed version', implying exact match including case.
    ]

    for test_str in test_strings:
        result = is_palindrome_optimized(test_str)
        print(f"'{test_str}' is {'a palindrome' if result else 'not a palindrome'}")