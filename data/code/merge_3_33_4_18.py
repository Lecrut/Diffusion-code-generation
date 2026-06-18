def filter_alphanumeric(text: str) -> str:
    """
    Returns a string containing only alphanumeric characters from the input,
    removing all spaces and other non-alphanumeric characters.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with only letters and digits remaining.
    """
    result = []
    for char in text:
        if char.isalnum():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    samples = [
        "Hello, World! 123",
        "Python@Code#Language_99",
        "   Spaces everywhere... and tabs\tand newlines\nhere!",
        ""
    ]

    for sample in samples:
        cleaned = filter_alphanumeric(sample)
        print(f"Input: '{sample}'")
        print(f"Output: '{cleaned}'\n")