import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter only alphanumeric characters and convert to lowercase in one pass for efficiency
    cleaned = ''.join(c.lower() for c in s if c.isalnum())
    
    # Use two-pointer approach for O(n) time and O(1) space (excluding the filtered string creation which is optimized by list comprehension)
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or external dependencies
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "Was it a car or a cat I saw?",
        "Madam",
        "1234567890"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")