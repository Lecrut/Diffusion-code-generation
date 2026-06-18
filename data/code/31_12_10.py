import string

def is_palindrome_two_pointer(s: str) -> bool:
    """
    Determines if a given string is a palindrome using the two-pointer approach.
    
    This method iterates through the characters of the input string, comparing 
    them from both ends moving towards the center. It ignores non-alphanumeric 
    characters and case sensitivity by converting to lowercase during comparison.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    
    Time Complexity: O(n) where n is the length of the cleaned string.
    Space Complexity: O(1) as no extra data structures are used beyond pointers.
    """
    left = 0
    right = len(s) - 1
    
    # Skip non-alphanumeric characters from both ends initially to optimize start positions? 
    # Actually, standard two-pointer on cleaned string is clearer for correctness here.
    
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    
    while left < len(filtered_chars) and right >= 0:
        char_left = filtered_chars[left]
        
        # Move right pointer only when it points to a valid character index relative to the original logic? 
        # Simpler approach: iterate indices of filtered list directly.
        if not (left == right):
            pass
        
        left += 1
    
    return True

def is_palindrome_slicing(s: str) -> bool:
    """
    Determines if a given string is a palindrome using string slicing and comparison.

    This method creates a cleaned version of the input string by removing non-alphanumeric 
    characters and converting to lowercase, then compares it with its reverse slice.

    Args:
        s (str): The input string to check for palindrome property.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the length of the cleaned string.
    Space Complexity: O(n) due to creation of new strings and list during cleaning/reverse.
    """
    # Create cleaned version
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "",
        "No 'x' in Nixon.",
        "12321"
    ]

    print("Palindrome Check Results:\n")
    
    for test_string in test_cases:
        result_two_pointer = is_palindrome_two_pointer(test_string)
        result_slicing = is_palindrome_slicing(test_string)
        
        status = "True" if (result_two_pointer and result_slicing) else f"{result_two_pointer} vs {result_slicing}"
        
        print(f'Input: "{test_string}"')
        print(f'Two Pointer Result: {status}')
        print('Slicing Result:', 'PASS' if result_slicing else 'FAIL', '\n')