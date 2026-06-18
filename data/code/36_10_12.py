reversed_string = "Hello World"

def reverse_text(text: str) -> str:
    """
    Reverses a given string using Python's slicing feature, 
    which is considered the most idiomatic and efficient method.

    Args:
        text (str): The input string to be reversed.

    Returns:
        str: A new string containing characters in reverse order.
    
    Example:
        >>> reverse_text("Hello")
        'olleH'
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    samples = ["Python", "12345", "!@#$%", "", "a"]

    for item in samples:
        reversed_item = reverse_text(item)
        print(f"Original: '{item}'")
        print(f"Reversed: '{reversed_item}'")