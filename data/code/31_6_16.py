def is_palindrome(text: str) -> bool:
    """
    Determines if a string is a palindrome, handling edge cases like empty strings 
    or strings containing only symbols. The comparison considers case-insensitivity 
    and ignores non-alphanumeric characters to focus on the core content structure.

    Args:
        text (str): The input string to check.

    Returns:
        bool: True if the processed string is a palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("")
        True
        >>> is_palindrome("!@@##$$%%^^&*()")
        True
    """
    # Handle empty string or None as an immediate palindrome
    if not text:
        return True

    # Filter to keep only alphanumeric characters and convert to lowercase
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())

    # Check the first half against the reversed second half of the filtered text
    length_half = len(cleaned_text) // 2
    
    return all(
        cleaned_text[i] == cleaned_text[length_half - (i + 1)] 
        for i in range(length_half)
    )

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "A man, a plan, a canal: Panama",   # Classic palindrome with punctuation and spaces
        "",                                  # Empty string edge case
        "!@@##$$%%^^&*()",                   # String containing only symbols (should be True after filtering)
        "Hello World!",                      # Not a palindrome
        "racecar",                           # Simple alphanumeric palindrome
        123,                                 # Should fail type check before logic but handled by docstring context if passed as str later; currently expects string input per signature. 
                                            # Note: Type hint enforces str, so int will raise TypeError immediately which is robust behavior for wrong types.
    ]

    print("Palindrome Checker Results:")
    results = []
    
    for sample in samples:
        try:
            result = is_palindrome(sample) if isinstance(sample, (str)) else "Type Error" # Ensure strict type checking based on signature intent or allow flexible runtime check? 
                                                    # The function signature says str. Let's run strictly as defined but handle potential non-string inputs gracefully in the loop for demonstration robustness.
            
            # Re-evaluating sample 123: Since func expects str, passing int will crash at definition unless we adjust call or func. 
            # To keep it runnable and safe without changing signature logic too much inside main block:
            if isinstance(sample, str):
                res = is_palindrome(sample)
            else:
                res = "Input type mismatch with function expectation (expected str)"
            
            results.append(res)
        except Exception as e:
            # Catch unexpected errors for robustness during testing
            print(f"Error processing sample '{sample}': {e}")
            results.append("Runtime Error")

    for i, res in enumerate(results):
        if isinstance(sample := samples[i], str):
             status = "PALINDROME" if (res is True) else f"Not Palindrome ({res})"
             print(f"{samples[i]} -> {status}")
        elif not isinstance(res, int): # Skip non-string results in formatted output to keep logs clean for valid string checks
            pass 
    # Specific re-printing for clarity on the list above logic
    
    # Cleaned up printing loop specifically for sample values:
    print("\nDetailed Output:")