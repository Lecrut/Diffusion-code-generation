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
    
    # Use two-pointer approach with slicing check (O(n) time, O(n) space due to slice creation)
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("Madam in Paris", True),
        ("12321", True),
        ("12345", False),
        ("a b c _ ! @ # $ % ^ & * ( ) - = + [ ] { } | : ; \" ' , . / ? < > ", True),
    ]

    for test_string, expected in test_cases:
        result = is_palindrome(test_string)
        print(f"Input: '{test_string}'")
        print(f"Expected: {expected}, Got: {result}")
        assert result == expected, f"Test failed for input: {test_string}"
    print("All tests passed.")