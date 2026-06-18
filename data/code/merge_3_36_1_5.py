def reverse_string(text: str) -> str:
    """
    Returns a new string with characters in reversed order using slicing notation.
    
    Args:
        text (str): The input string to be reversed.
        
    Returns:
        str: A new string containing the characters of 'text' in reverse order.
    """
    return text[::-1]

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies
    samples = [
        "Hello, World!",
        "",
        "a",
        "Python is awesome.",
        12345 if False else None  # This line ensures no type errors; logic handled by function below
    ]

    for sample in ["Hello, World!", "python", ""]:
        result = reverse_string(sample)
        print(f"Original: '{sample}'")
        print(f"Reversed: '{result}'\n")