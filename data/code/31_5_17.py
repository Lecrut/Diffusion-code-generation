def is_palindrome(s: str) -> bool:
    """
    Check if a string is a palindrome using the two-pointer technique.
    
    This function compares characters from both ends of the string moving 
    towards the center, ignoring non-alphanumeric characters and case sensitivity.
    
    Args:
        s (str): The input string to check
        
    Returns:
        bool: True if the string is a palindrome, False otherwise
    
    Time Complexity: O(n) where n is the length of the string
    Space Complexity: O(1) as we only use two pointers and no extra data structures
    """
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer to next alphanumeric character
        if not s[left].isalnum():
            left += 1
            continue
        
        # Move right pointer to previous alphanumeric character
        if not s[right].isalnum():
            right -= 1
            continue
            
        # Compare characters (case-insensitive)
        if s[left].lower() != s[right].lower():
            return False
            
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    test_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "hello"
    ]
    
    results = []
    for test_str in test_strings:
        result = is_palindrome(test_str)
        results.append(f"'{test_str}' -> {result}")
    
    # Print all results separated by newlines
    print('\n'.join(results))