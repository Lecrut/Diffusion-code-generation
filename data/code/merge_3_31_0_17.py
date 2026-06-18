def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon.", True),
        ("Hello, World!", False),
    ]

    for input_str, expected in test_cases:
        result = is_palindrome(input_str)
        status = "PASS" if result == expected else "FAIL"
        print(f"{status}: '{input_str}' -> {result} (expected {expected})")