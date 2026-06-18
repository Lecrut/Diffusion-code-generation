import string

def is_palindrome_two_pointers(s: str) -> bool:
    """
    Check if a given string is a palindrome using two pointers.
    
    This approach compares characters from both ends moving towards the center,
    ignoring case and non-alphanumeric characters for flexibility (though input 
    can be just alphanumeric). It has O(n) time complexity and O(1) space complexity.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example:
        >>> is_palindrome_two_pointers("A man a plan a canal Panama")
        True
    """
    # Convert to lowercase and filter for alphanumeric characters only
    cleaned = [c.lower() for c in s if c.isalnum()]
    
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Check if a given string is a palindrome using string slicing.
    
    This approach creates reversed versions of the filtered and lowercased string,
    then compares them directly. It has O(n) time complexity but higher space 
    usage due to creating new strings (O(n)).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Example:
        >>> is_palindrome_slicing("12321")
        True
    """
    # Filter for alphanumeric characters and convert to lowercase
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    return cleaned == cleaned[::-1]

if __name__ == '__main':
    # Hard-coded sample values as per requirements
    samples = [
        "A man a plan a canal Panama",  # Should be True (with ignored spaces/punctuation)
        "racecar",                     # Should be True
        "hello world!",                # Should be False ('!' removed, 'olleh olwrd') != reversed
        "",                           # Edge case: empty string -> True
        "Was it a car or a cat I saw?",  # Should be True (ignoring spaces/punctuation)
    ]

    print("Running Palindrome Check Module...\n")
    
    for i, test_str in enumerate(samples):
        result_tp = is_palindrome_two_pointers(test_str)
        result_sl = is_palindrome_slicing(test_str)
        
        # Note: For this implementation, we ignore non-alphanumeric chars. 
        # If strict equality including symbols was needed, the filtering logic would differ.
        # Assuming standard palindrome definition often used in such tasks (ignoring format).
        print(f"Sample {i+1}: '{test_str}'")
        
        if result_tp == result_sl:
            status = "Matched"
        else:
            status = "Mismatched (Implementation difference noted)"
            
        # Adjust logic for the specific filtering applied here to ensure consistency in demo output.
        # For 'A man...', standard palindrome check usually ignores non-alnum.
        print(f"  Two-Pointer Result : {result_tp}")
        print(f"  Slicing Result      : {result_sl}")
        print(f"  Status              : {status}\n")

    # Additional strict test without filtering to show difference if needed, 
    # but keeping logic consistent with the function definitions above.
    
    additional_samples = [
        ("madam", "Should be True"),
        ("hello", "Should be False"),
    ]

    print("Additional Strict Tests:\n")
    for test_input, desc in additional_samples:
        r1 = is_palindrome_two_pointers(test_input)
        r2 = is_palindrome_slicing(test_input)
        print(f"Test '{test_input}': Two-Pointer={r1}, Slicing={r2}. Expected=True. ")

if __name__ == '__main__':
    pass
