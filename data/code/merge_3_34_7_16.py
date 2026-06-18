def capitalize_words(text: str) -> str:
    """
    A decorator-like function that automatically capitalizes 
    the first letter of every word in a string.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with each word's first character capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    # Split the string into words while preserving whitespace structure isn't explicitly requested 
    # but typically 'capitalize_words' implies splitting by whitespace and joining back.
    return " ".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "hello world",
        "this is a python script",
        "   multiple spaces between words  ",
        "alreadyCapitalized"
    ]

    for sample in samples:
        result = capitalize_words(sample)
        print(f'Input: "{sample}"')
        print(f'Output: "{result}"\n')