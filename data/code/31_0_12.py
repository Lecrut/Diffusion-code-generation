def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    filtered = ''.join(char.lower() for char in s if char.isalnum())
    return filtered == filtered[::-1]

if __name__ == '__main__':
    # Sample test cases with no user input required
    samples = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "Was it a car or a cat I saw?",
        "",
        "No 'x' in Nixon.",
        "Not a palindrome"
    ]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")