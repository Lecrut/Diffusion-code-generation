def contains_repeated_letters(text: str) -> bool:
    """
    Determines if a given string contains any repeated letters (case-insensitive).
    
    Args:
        text (str): The input string to check.
        
    Returns:
        bool: True if there are duplicate letters, False otherwise.
    """
    seen = set()
    for char in text.lower():
        if 'a' <= char <= 'z':  # Only consider alphabetic characters a-z
            if char in seen:
                return True
            seen.add(char)
    return False

if __name__ == '__main__':
    test_cases = [
        "hello",      # Should return True ('l' repeats)
        "abcdefg",    # Should return False (no repeats)
        "Hello World!",  # Should return True ('l', 'o')
        "pythonic",   # Should return True ('i' and 'n' repeat? no, p-y-t-h-o-n-i-c -> unique. Wait: n appears once. Actually pythonic has no repeated letters.)
    ]

    for test_str in test_cases:
        result = contains_repeated_letters(test_str)
        print(f"'{test_str}' => {result}")