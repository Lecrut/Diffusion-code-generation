import re

def is_palindrome(s: str) -> bool:
    """
    Returns True if the input string is a palindrome, ignoring case 
    and non-alphanumeric characters. Otherwise returns False.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if s is a palindrome after normalization, False otherwise.
    """
    # Extract alphanumeric characters from the string and convert to lowercase
    cleaned_string = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the normalized string matches its reverse
    return cleaned_string == cleaned_string[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a cat and I saw a raccoon?", True),
        ("No 'x' in Nixon.", True),
        ("123 21", True),
        ("hello", False),
    ]

    for test_input, expected_result in test_cases:
        result = is_palindrome(test_input)
        print(f"Input: '{test_input}'")
        print(f"Expected: {expected_result}, Got: {result}")
        
        if result != expected_result:
            print("ERROR: Test case failed!")
        else:
            print("OK\n")