def capitalize_first_word(text):
    """
    Decorator-like function that capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    # Split the string into words, capitalize the first character of each, then join them back
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return ' '.join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Sample usage demonstrating functionality without any user input or external dependencies
    
    sample_strings = [
        "hello world",
        "python programming is fun",
        "this   has   multiple      spaces",
        "singleword",
        ""  # Edge case: empty string
    ]

    for original in sample_strings:
        capitalized_result = capitalize_first_word(original)
        print(f"Input: '{original}'")
        print(f"Output: '{capitalized_result}'\n")