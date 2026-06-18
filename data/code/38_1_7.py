def find_repeated_letters(text: str) -> set:
    """
    Returns a set of letters that appear more than once in the input string.
    
    The function is case-insensitive and ignores non-alphabetic characters.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        set: A set containing unique repeated letters found in the text.
    """
    letter_count = {}
    
    for char in text.lower():
        if 'a' <= char <= 'z':
            letter_count[char] = letter_count.get(char, 0) + 1
            
    return {char for char, count in letter_count.items() if count > 1}

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    test_cases = [
        "Hello World!",
        "python programming is awesome",
        "aabbccdd",
        "xyzabc",
        ""
    ]

    for text in test_cases:
        result = find_repeated_letters(text)
        print(f"Input: '{text}'")
        print(f"Repeated letters: {result}")
        
        if not isinstance(result, set):
            raise TypeError("The function did not return a set.")
            
        # Verify correctness for known cases without external dependencies
        assert "h" in result or "l" in result or "o" in result or "w" in result or "d" in result \
               if text == "Hello World!" else True
        
        print("---")