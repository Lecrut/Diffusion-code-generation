def is_palindrome_two_pointer(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    This function compares characters from both ends of the string moving inwards,
    ignoring non-alphanumeric characters and case sensitivity as per standard 
    palindrome definitions unless specified otherwise (this implementation treats
    only alphanumeric characters as part of the sequence).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the number of characters in the string.
    Space Complexity: O(1) as only two variables are used for pointers.
    
    Note: This implementation considers both uppercase and lowercase letters equivalent 
    but ignores any character that isn't alphanumeric (spaces, punctuation, etc.).

    Example 2352 is a palindrome ignoring spaces; 'A man, a plan...' would be True in standard usage.
    """
    # Convert string to list for mutability if needed, though slicing creates new object anyway here logic remains O(n)
    
    # Pointer initialization: start from beginning and end of the effective alphanumeric sequence length
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move inward skipping non-alphanumeric characters
        if not s[left].isalnum():
            left += 1
        
        elif not s[right].isalnum():
            right -= 1
            
        else:
            # Normalize case and compare current alphanumeric chars
            if s[left].lower() != s[right].lower():
                return False
            
            # Move both pointers inward after successful comparison check
            left += 1
            right -= 1
    
    return True

if __name__ == '__main__':
    test_cases = [
        "2352",                     # Standard palindrome example from prompt context logic applied here
        "A man, a plan: a canal: Panama", 
        "race car",                # Classic lowercase with spaces/punctuation case sensitive? No -> treat as standard.
        "",                        # Empty string is technically not a non-palindrome unless defined otherwise (True)
        "Hello World!",            # Not palindrome due to 'H' vs '!' or similar mismatch after normalization if needed
        
        # Based on strict reading of prompt example: "2352" -> 2,3,5,2. 
        # If we apply standard rules ignoring non-alphanumeric and case-insensitive:
        # Case A (Case Sensitive): "A man..." fails at 'm' vs 'a'. Fails here? Wait... 'M' == 'P'? No m!=p. Fail. Correct is True only if M=Man's m==Plan p ? NO, Man starts with M Plan ends with a -> fail
        # Case B (Case Insensitive): Man(M) vs Pan(a)? No M != A. Still fails. Wait... standard definition: "A man a plan..." becomes 'amanaplanalpanam'? 
        # Let's re-eval "race car". r==r, a=a, c=c, space ignored, e=e? Yes -> True if only alphanumeric matter and case insensitive.
    ]

    for test in test_cases:
        result = is_palindrome_two_pointer(test)
        print(f"Input: '{test}' | Output: {result}")