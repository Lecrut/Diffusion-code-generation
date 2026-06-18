def capitalize_words(text: str) -> str:
    """
    A decorator that automatically capitalizes the first letter of every word in a string.
    
    Args:
        text (str): The input string to be processed.
        
    Returns:
        str: The capitalized version of the input string.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "this is a test case",
        "python programming language"
    ]
    
    print("Original Strings and Capitalized Versions:")
    print("-" * 40)
    for original in sample_strings:
        capitalized = capitalize_words(original)
        print(f"Input:      '{original}'")
        print(f"Output:     '{capitalized}'")
        print("-" * 40)