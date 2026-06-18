import re

def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    # Keep only alphanumeric characters and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    
    # Check if the cleaned string reads the same forwards and backwards
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        ("Was it a car or a cat I saw?", True),
        ("No 'x' in Nixon", True),
        ("Hello, World!", False),
        ("", True),
        ("a", True),
    ]

    for test_input, expected_result in test_cases:
        result = is_palindrome(test_input)
        print(f"Input: '{test_input}'")
        print(f"Expected: {expected_result}, Got: {result}")
        assert result == expected_result, f"Test failed for input: {test_input}"
    print("All tests passed.")