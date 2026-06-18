def capitalize_first_letters(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string.
    
    This function splits the input text into words, capitalizes the 
    first character of each word (if it is alphabetic), and joins them back together with spaces.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized.
    """
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_strings = [
        "hello world",
        "python programming is fun",
        "multi-word sentence here.",
        "  leading spaces and trailing   ",
        "UPPERCASE mixed case"
    ]

    for s in sample_strings:
        result = capitalize_first_letters(s)
        print(f'Input: "{s}"')
        print(f'Output: "{result}"\n')