import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter only alphanumeric characters and convert to lowercase for comparison
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Use two-pointer approach for O(n) time complexity without extra space beyond input processing
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
        "Was it a cat and I saw a raccoon?",
        "No 'x' in Nixon.",
        "12321",
        "Hello, World!",
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")