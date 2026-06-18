import re

def is_palindrome(s: str) -> bool:
    """
    Returns True if the input string is a palindrome, considering case-insensitivity 
    and ignoring non-alphanumeric characters. Otherwise returns False.
    
    The function uses two pointers moving towards each other to optimize space complexity O(1).
    Time complexity is O(n), where n is the length of the string after filtering or processing.

    Args:
        s (str): Input string to check.

    Returns:
        bool: True if palindrome, False otherwise.
    """
    # Convert to lowercase and filter for alphanumeric characters in one pass using regex compilation outside loop 
    pattern = re.compile(r'[a-zA-Z0-9]')
    
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Move left pointer until an alphanumeric char is found or pointers meet/cross
        while left < right and not pattern.match(s[left]):
            left += 1
        
        # Move right pointer until an alphanumeric char is found or pointers meet/cross
        while left < right and not pattern.match(s[right]):
            right -= 1
        
        if s.lower()[left] != s.lower()[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    # Sample tests run without user input, command-line arguments, network access, or pre-existing files.
    
    test_cases = [
        ("A man a plan a canal Panama", True),
        ("race a car", False),
        ("Was it a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("hello world!", False),
        ("123454321", True),
        ("Madam", True),
        ("Not a palindrome", False)
    ]

    for test_input, expected_output in test_cases:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected_output else "FAIL"
        
        # Print results to verify functionality; using print avoids interactive prompts as per requirements.
        print(f"{status}: '{test_input}' -> {result}")