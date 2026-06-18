def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring case and non-alphanumeric characters.
    
    Args:
        s (str): The input string to check.
        
    Returns:
        bool: True if the string is a palindrome, False otherwise.
    """
    filtered_chars = [c.lower() for c in s if c.isalnum()]
    return filtered_chars == filtered_chars[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to test without user input or external dependencies
    samples = ["Racecar!", "A man, a plan, a canal: Panama", "Hello World", "Was it a car or a cat I saw?", "!_a_b"]

    for sample in samples:
        result = is_palindrome(sample)
        print(f"'{sample}' -> {result}")