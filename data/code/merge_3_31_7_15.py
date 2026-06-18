def is_palindrome_optimized(s: str) -> bool:
    """Check if a string is a palindrome by comparing original with reversed version efficiently."""
    # In Python, slicing creates a copy, but it's optimized in CPython and minimal for typical inputs.
    # This approach ensures readability while maintaining the core requirement of reversing.
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed
    test_cases = [
        "radar",           # True palindrome
        "hello",           # False palindrome
        "",                # Empty string is technically a palindrome (True)
        "A man a plan a canal Panama",  # Needs normalization? Task specifies direct reversal comparison. Keeping as-is -> False due to spaces/case unless specified otherwise. 
                           # Based on strict interpretation: comparing original with reversed version exactly.
    ]

    for test_str in test_cases:
        result = is_palindrome_optimized(test_str)
        print(f"String: '{test_str}' | Is Palindrome: {result}")