def filter_alphanumeric(text: str) -> str:
    """
    Returns a new string containing only alphanumeric characters from the input.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A string with all non-alphanumeric and whitespace characters removed.
    """
    return ''.join(char for char in text if char.isalnum())

if __name__ == '__main__':
    # Sample inputs as hard-coded values; no user input or external dependencies required
    sample_strings = [
        "Hello, World! 123",
        "Test@# $%^ &* ()_+" ,
        "   Leading and trailing spaces with tabs\tand newlines\nhere"
    ]

    for original in sample_strings:
        filtered_result = filter_alphanumeric(original)
        print(f"Input: '{original}'")
        print(f"Output: '{filtered_result}'\n")