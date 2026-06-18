def is_palindrome(s: str) -> bool:
    """
    Returns True if the input string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if palindrome, False otherwise.
    """
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input or network access
    samples = [
        "A man, a plan, a canal: Panama",  # True
        "race a car",                        # False
        "",                                # True (empty string is palindrome)
        "Was it a cat and I saw a raccoon?",# True
        "Madam",                            # True
    ]

    for test_str in samples:
        result = is_palindrome(test_str)
        print(f'"{test_str}" -> {result}')