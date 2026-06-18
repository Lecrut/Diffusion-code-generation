def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in a string.
    
    This function uses Python's built-in split() to tokenize the input 
    by whitespace and list comprehension with capitalization logic,
    avoiding manual indexing loops for efficiency and readability.
    
    Args:
        text (str): The input string containing words.
        
    Returns:
        str: A new string with each word capitalized.
    """
    return " ".join(word.capitalize() if word else "" for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "hello world",
        "python is awesome and fun!",
        "  multiple   spaces between words ",
        "",
        "single"
    ]

    for original in samples:
        result = capitalize_words(original)
        print(f'Input: "{original}"')
        print(f'Output: "{result}"\n')