def capitalize_first_word(text: str) -> str:
    """
    Decorator-like function that capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    # Split the string into words based on whitespace
    words = text.split()
    # Capitalize the first letter of each non-empty word and join them back with spaces
    capitalized_words = [word.capitalize() for word in words]
    return ' '.join(capitalized_words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python is awesome",
        "the quick brown fox jumps over the lazy dog",
        "multiple   spaces  between  words"
    ]

    for original in sample_strings:
        result = capitalize_first_word(original)
        print(f'Original: "{original}"')
        print(f'Result: "{result}"\n')