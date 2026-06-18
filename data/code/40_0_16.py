import string

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first letter of each word from the input text.
    
    Handles various whitespace scenarios (multiple spaces, tabs, newlines).
    Ignores non-alphabetic characters when determining what constitutes a 'word'.
    Returns a list of single-character strings representing the first letters.
    
    Args:
        text: The input string to process.
        
    Returns:
        A list containing the first alphabetic character of each word found in the text.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split by any whitespace (spaces, tabs, newlines) and filter out empty strings
    words = [word for word in text.split() if len(word.strip()) > 0]
    
    first_letters = []
    
    for word in words:
        # Iterate through characters to find the first alphabetic one
        found_letter = False
        for char in word:
            if char.isalpha():
                first_letters.append(char)
                found_letter = True
                break
        
        # If no letters were found in a "word" (e.g., symbols only), skip it.
        # This ensures we don't return non-letter characters as the 'first letter'.
    
    return first_letters

if __name__ == '__main__':
    sample_text = """
    Hello World! 
      Python is great...   And so are you?
    
       No letters here: 12345.
      
         One word here. Two words there!!!
    """

    result = get_first_letters(sample_text)
    
    print("Input text:")
    print(repr(sample_text))
    print("\nFirst letter of each alphabetic word:")
    for i, char in enumerate(result):
        # Using f-string with a newline separator if list is long enough to be readable on one line isn't ideal here.
        # Just printing the result joined by spaces or newlines depending on length logic usually seen in such tasks.
        pass
    
    print("".join(result))
    
    # Verification for specific edge cases mentioned implicitly (symbols, numbers)
    test_case_1 = "a b c"
    assert get_first_letters(test_case_1) == ['a', 'b', 'c'], f"Failed: {get_first_letters(test_case_1)}"
    
    test_case_2 = "!@#$%^&*()"
    assert get_first_letters(test_case_2) == [], f"Failed: {get_first_letters(test_case_2)}"
    
    print("\nAll assertions passed.")