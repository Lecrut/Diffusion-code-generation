def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the casing of all other letters. Handles edge cases
    such as empty strings and leading/trailing whitespace.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only the first letter of each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split into words based on whitespace
    raw_words = text.split()
    
    def capitalize_first_char(word: str) -> str:
        """Helper function to capitalize the first letter of a non-empty word."""
        if not word:
            return word
        
        # Check if it's already capitalized (optional strictness check, 
        # but task implies simple 'capitalize' behavior unless specified otherwise).
        # The standard `capitalize()` method lowercases the rest which might violate 
        # "preserving the rest of the casing". However, Python's built-in `.capitalize()`
        # is usually what is expected. Let's implement strictly based on prompt:
        # "capitalizes only the first letter ... preserving the rest".
        if len(word) == 1:
            return word.upper()
        
        first_char = word[0]
        remaining_chars = ''.join(c for c in word[1:] if not (c.islower() or ('A' <= c <= 'Z'))) + \
                          ''.join(c for c in word[1:]) # This logic is flawed, let's simplify
        
        # Re-evaluating strict interpretation: 
        # "Capitalizes only the first letter" -> make it uppercase.
        # "Preserving the rest of the casing" -> keep original case for subsequent letters.
        
        if not first_char.isalpha():
            return word
            
        capitalized_first = first_char.upper()
        remaining_part = word[1:] 
        return capitalized_first + ''.join(c.lower() if c.isupper() else c)

    # Actually, the prompt likely implies standard Title Case but preserving existing capitalization logic.
    # Standard behavior: "Hello WORLD" -> "Hello World".
    # If we strictly preserve casing of 'W', it remains 'W'. 
    # The phrase "preserving the rest of the casing" usually means if you have "hElLo", result is "HElLo"? 
    # No, that would be changing the first letter to uppercase. 
    # It implies: Input -> Output where only index 0 (of word) changes case from potentially lower to upper, others stay same.
    
    processed_words = [word[0].upper() + ''.join(char if char.isalpha() else char for char in word[1:]) 
                       for word in raw_words]

    return ' '.join(processed_words)

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "hello world",
        "python scripting is fun.",
        "   leading spaces  ",
        "",
        "UPPERCASE and mixedCase"
    ]

    for test_input in samples:
        print(f"Input: '{test_input}'")
        result = capitalize_words(test_input)
        print(f"Output: '{result}'")
        print("-" * 30)