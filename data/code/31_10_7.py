import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Time Complexity: O(n), where n is the length of the input string.
    Space Complexity: O(1), as we modify the input in place using two pointers without creating new strings 
                     (the regex compilation creates one cached pattern object).

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Compile regex once for efficiency; it matches alphanumeric characters in ASCII and Unicode categories
    alnum_pattern = re.compile(r'\w', flags=re.UNICODE)
    
    left, right = 0, len(s) - 1
    
    while left < right:
        if not alnum_pattern.match(s[left]):
            left += 1
            continue
            
        if not alnum_pattern.match(s[right]):
            right -= 1
            continue
        
        # Compare characters after converting to lowercase for case-insensitivity
        if s[left].lower() != s[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        "",
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon.", True),
        ("12321", True),
        ("Hello World!", False)
    ]

    for test_input, expected_result in test_cases:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"[{status}] Input: '{test_input}' -> Output: {result}")