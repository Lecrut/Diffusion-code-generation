def case_swap(text: str) -> dict[str, str]:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' 
    to their respective case transformations of the input string.
    
    Args:
        text (str): The input string to transform.
        
    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', 'title'.
    """
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    lower_text = text.lower()
    upper_text = text.upper()
    
    # Title case converts the first character of each word to uppercase 
    # and the rest to lowercase. This is generally more readable for natural language.
    title_text = text.title()

    return {
        'lower': lower_text,
        'upper': upper_text,
        'title': title_text
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.
    samples = [
        "Hello World",
        "python programming is fun!",
        "123 Main Street"
    ]

    for text in samples:
        result = case_swap(text)
        print(f"\nInput: {text}")
        print("Lowercase:", result['lower'])
        print("Uppercase:", result['upper'])
        print("Title Case:", result['title'])