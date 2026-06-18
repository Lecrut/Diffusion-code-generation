def remove_whitespace_generator(text):
    """
    Generator function that yields characters from input string excluding whitespace.
    
    Args:
        text (str): The input string to process
        
    Yields:
        str: Individual non-whitespace characters
    """
    for char in text:
        if not char.isspace():
            yield char

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    samples = [
        "Hello World",
        "Python 3.9 is great!",
        "   Leading spaces here"
    ]
    
    for sample in samples:
        print(f"\nOriginal: '{sample}'")
        result = remove_whitespace_generator(sample)
        
        # Convert generator to list and join with space for display
        cleaned_chars = ''.join(result)
        print(f"Cleaned:  '{cleaned_chars}'")