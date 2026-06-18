def capitalize_words(text: str) -> str:
    """
    Capitalizes the first letter of each word in the input string,
    preserving the case of all other characters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")
    
    return "".join(word.capitalize() for word in text.split())

if __name__ == '__main__':
    sample_text = "hello world this is an example of capitalization."
    result = capitalize_words(sample_text)
    print(result)

# Expected output: Hello World This Is An Example Of Capitalization.