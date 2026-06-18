import re

def is_palindrome(s: str) -> bool:
    """
    Returns True if the string s is a palindrome, ignoring case 
    and non-alphanumeric characters. Otherwise returns False.
    
    Optimized by using two pointers to traverse from both ends towards center,
    O(n/2) time complexity compared to creating intermediate lists which are more expensive.
    Space complexity: O(1).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if palindrome, False otherwise.
    
    Examples:
        >>> is_palindrome("A man, a plan, a canal: Panama")
        True
        >>> is_palindrome("race a car")
        False
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Skip non-alphanumeric characters from the left
        if not s[left].isalnum():
            left += 1
            continue
        
        # Skip non-alphanumeric characters from the right
        if not s[right].isalnum():
            right -= 1
            continue

        # Compare lowercase versions of current characters
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    test_cases = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "No 'x' in Nixon",
        "Was it a car or a cat I saw?",
        "12321",
        "1234567890"
    ]

    print("Palindrome Check Results:")
    for text in test_cases:
        result = is_palindrome(text)
        print(f'{text!r}: {result}')