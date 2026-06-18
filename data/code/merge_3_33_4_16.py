def filter_alphanumeric(text: str) -> str:
    """
    Returns a new string containing only alphanumeric characters from the input.
    All spaces, punctuation, symbols, and other non-alphanumeric characters are removed.

    Args:
        text (str): The input string to process.

    Returns:
        str: A filtered string with only letters and digits remaining in order.
    """
    result = []
    for char in text:
        if char.isalnum():
            result.append(char)
    return ''.join(result)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "Hello, World! 123",
        "Python@Programming#2024!",
        "   Spaces everywhere... and tabs\tand newlines\nhere.",
        "No special chars here just letters ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    ]

    for sample in samples:
        cleaned = filter_alphanumeric(sample)
        print(f"Original: {sample!r}")
        print(f"Filtered : {cleaned!r}\n")