def filter_alphanumeric(text: str) -> str:
    """
    Returns a string containing only alphanumeric characters from the input.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with all spaces and non-alphanumeric characters removed.
    """
    return ''.join(char for char in text if char.isalnum())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or files)
    test_strings = [
        "Hello World! 123",
        "Python@Code#99 & Spaces   ",
        "Mixed: Case _ and Numbers 456!"
    ]

    for original in test_strings:
        result = filter_alphanumeric(original)
        print(f"Input: '{original}'")
        print(f"Output: '{result}'\n")