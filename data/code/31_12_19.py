def is_palindrome_two_pointers(s: str) -> bool:
    """
    Determines if a string is a palindrome using the two-pointer approach.
    Compares characters from both ends moving towards the center, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    left = 0
    right = len(s) - 1
    
    # Normalize by converting to lowercase and filtering for alphanumeric characters
    s_normalized = ''.join(c.lower() for c in s if c.isalnum())
    
    while left < right:
        if s_normalized[left] != s_normalized[right]:
            return False
        left += 1
        right -= 1
    
    return True

def is_palindrome_string_slicing(s: str) -> bool:
    """
    Determines if a string is a palindrome using string slicing.
    Compares the normalized string with its reverse.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome after normalization, False otherwise.
    """
    # Normalize by converting to lowercase and filtering for alphanumeric characters
    s_normalized = ''.join(c.lower() for c in s if c.isalnum())
    
    return s_normalized == s_normalized[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon.",
        "Madam",
        "Hello"
    ]

    print("Palindrome Check Results:")
    for test_string in test_cases:
        result_two_pointer = is_palindrome_two_pointers(test_string)
        result_slicing = is_palindrome_string_slicing(test_string)
        
        status = "Is Palindrome" if (result_two_pointer and result_slicing) else "Not a Palindrome"
        print(f'"{test_string}" -> {status}')

    # Verify consistency between the two methods for all test cases.
    assert all(is_palindrome_two_pointers(tc) == is_palindrome_string_slicing(tc) 
               for tc in test_cases), "The two implementations produced inconsistent results."
    
    print("\nAll tests passed: Both implementations are consistent.")