def is_palindrome_two_pointers(s: str) -> bool:
    """
    Determines if a string is a palindrome using a two-pointer approach.
    
    This method iterates from both ends of the string towards the center,
    comparing characters at each step to determine palindromic property efficiently.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Compare characters at current pointers
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
        
    return True

def is_palindrome_string_slicing(s: str) -> bool:
    """
    Determines if a string is a palindrome using string slicing.
    
    This method checks if the reversed version of the original string matches
    itself, which inherently handles symmetry detection in an optimized manner for Python strings.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    return s == s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    
    test_cases = [
        "racecar",           # Expected: True
        "hello",             # Expected: False
        "",                  # Expected: True (empty string is palindrome)
        "A man a plan a canal Panama",  # Note: Spaces included in this check. 
                             # For case-insensitive/ignore-space, logic would need extension.
                             # Here we stick to strict character matching as per standard definition unless specified otherwise.
    ]

    print("Testing Two-Pointer Approach:")
    for test_str in test_cases:
        result = is_palindrome_two_pointers(test_str)
        status = "Palindrome" if result else "Not a Palindrome"
        print(f"'{test_str}' -> {status}")

    print("\nTesting String Slicing Approach:")
    for test_str in test_cases:
        result = is_palindrome_string_slicing(test_str)
        status = "Palindrome" if result else "Not a Palindrome"
        print(f"'{test_str}' -> {status}")