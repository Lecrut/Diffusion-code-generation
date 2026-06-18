def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Filter only alphanumeric characters and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon.", True),
        ("Hello, World!", False),
        ("", True),
        ("a", True),
    ]

    for test_input, expected_result in test_cases:
        result = is_palindrome(test_input)
        status = "PASS" if result == expected_result else "FAIL"
        print(f"{status}: '{test_input}' -> {result} (Expected: {expected_result})")