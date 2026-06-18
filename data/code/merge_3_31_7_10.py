def is_palindrome_optimized(s: str) -> bool:
    """
    Check if a string is a palindrome by comparing characters from both ends moving inward.
    
    This approach avoids creating a reversed copy of the string, thus minimizing memory usage.
    It only iterates through half the length of the string and compares corresponding indices.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Time Complexity: O(n) where n is the number of characters in the string.
    Space Complexity: O(1) as no additional data structures proportional to input size are used.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [
        "radar",           # Expected: True
        "racecar",         # Expected: True
        "hello",           # Expected: False
        "A man a plan a canal Panama",  # Expected: False (due to spaces and case sensitivity unless specified otherwise)
        "",                # Edge case: Empty string, expected: True
        "12321"            # Numeric palindrome
    ]

    print("Palindrome Check Results:")
    for test_str in test_cases:
        result = is_palindrome_optimized(test_str)
        status = "is a palindrome" if result else "is NOT a palindrome"
        print(f"'{test_str}' {status}")