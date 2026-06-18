def capitalize_words(text: str) -> str:
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
    capitalized_words = [word.capitalize() if len(word) > 0 else "" for word in words]
    
    return " ".join(capitalized_words)

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python is awesome!",
        "   multiple      spaces here ",
        "singleword"
    ]

    for original in sample_strings:
        result = capitalize_words(original)
        print(f'Input: "{original}"')
        print(f'Output: "{result}"\n')