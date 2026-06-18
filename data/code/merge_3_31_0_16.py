def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring case, spaces, punctuation, 
    and other non-alphanumeric characters.

    Args:
        s (str): The input string to check.

    Returns:
        bool: True if the cleaned string reads the same forwards and backwards, False otherwise.
    """
    # Filter only alphanumeric characters and convert to lowercase
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    
    # Join into a single string (or use two pointers on list)
    clean_string = "".join(filtered_chars)

    return clean_string == clean_string[::-1]

if __name__ == '__main__':
    test_cases = [
        "A man, a plan, a canal: Panama",  # Should be True
        "race a car",                       # Should be False
        "Was it a car or a cat I saw?",   # Should be True
        "",                                # Should be True (empty string)
        "No 'x' in Nixon",                  # Should be True
    ]

    for test_input in test_cases:
        result = is_palindrome(test_input)
        print(f"'{test_input}' -> {result}")