def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    filtered_s = ''.join(char.lower() for char in s if char.isalnum())
    return filtered_s == filtered_s[::-1]

if __name__ == '__main__':
    sample_strings = [
        "A man, a plan, a canal: Panama",
        "race a car",
        "",
        "_!@#$%^&*()_!@#",
        "Was it a car or a cat I saw?",
        "No 'x' in Nixon"
    ]

    for sample_str in sample_strings:
        result = is_palindrome(sample_str)
        print(f"'{sample_str}' -> {result}")