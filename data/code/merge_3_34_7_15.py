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
    
    # Split the string into words based on whitespace, capitalize each, then join back
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is an example sentence with mixed case",
        "python programming language",
        ""  # Edge case: empty string
    ]

    print("Original String | Capitalized Result")
    print("-" * 50)
    
    for original in sample_strings:
        result = capitalize_words(original)
        print(f"{original!r:<32} | {result}")