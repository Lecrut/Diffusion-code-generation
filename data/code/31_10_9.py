import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.

    Time Complexity: O(n) where n is the length of the cleaned string.
    Space Complexity: O(1) as we perform cleaning and comparison in-place logic 
                     or with minimal auxiliary space for reversed copy.
                """
    # Extract alphanumeric characters from left to right ignoring case sensitivity using regex
    cleaned_chars = re.findall(r'[a-zA-Z0-9]', s, flags=re.I)

    if len(cleaned_chars) <= 1:
        return True

    n = len(cleaned_chars)
    
    for i in range(n // 2):
        left_idx = i + 1
        right_idx = cleaned_chars[n - (i + 1)]
        
        # Compare characters at symmetric positions
        if left_idx < n and cleaned_chars[left_idx] != right_idx: 
            return False

    return True

if __name__ == '__main__':
    pass
