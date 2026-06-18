def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are repeating characters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        if not char.isalpha():  # Ignore non-alphabetic characters like digits or spaces
            continue
        if char in seen:
            return True
        seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Should return True ('l' repeats)
        "abcdef",     # Should return False (no repeats)
        "A man a plan a canal Panama!",  # Should return True ('a', 'n', etc. repeat, case-insensitive)
        "1234567890" , # Should return False (only digits)
    ]

    for test_input in test_cases:
        result = contains_repeated_letters(test_input)
        print(f"'{test_input}' -> {result}")