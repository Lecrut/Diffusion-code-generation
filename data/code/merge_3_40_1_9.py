def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of every word in the input string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        List[str]: A list of single-character strings representing the first 
                   letters of each word found in the text. Words are defined as 
                   sequences of non-whitespace characters, and only alphabetic 
                   starting characters are included if a word does not start with one.
    
    Note: This implementation uses regex to robustly identify words regardless 
        of casing or punctuation attached to them. If a 'word' starts with a 
        non-alphabetic character (like numbers), it is skipped unless specified otherwise,
        but standard English usage implies alphabetic starting letters are expected for "first letter".
    """
    import re
    
    # Split the text into words based on whitespace
    raw_words = text.split()
    
    first_letters = [word[0].lower() if word and word[0].isalpha() else '' 
                     for word in raw_words]
    
    return first_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or files.
    test_strings = [
        "Hello World",
        "Python Programming Language",
        "  Multiple   Spaces ",
        "",
        "123 Numbers! Are Not Letters.",
        "A B C D E"
    ]

    for sample in test_strings:
        result = get_first_letters(sample)
        print(f"'{sample}' -> {result}")