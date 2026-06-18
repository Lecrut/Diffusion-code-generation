def is_palindrome(s: str) -> bool:
    """
    Determines if a given string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    # Filter for alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # Compare the list from start to end (using two-pointer logic implicitly via slicing)
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    test_cases = ["A man, a plan, a canal: Panama", "No 'x' in Nixon", "Not A Palindrome"]
    
    for string in test_cases:
        result = is_palindrome(string)
        print(f"'{string}' -> {result}")