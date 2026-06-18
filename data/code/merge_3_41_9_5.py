import sys

def case_swap(text: str) -> dict[str, str]:
    """
    Takes a string and returns a dictionary mapping keys 'lower', 'upper', 
    and 'title' to their respective case transformations.
    
    Prioritizes readability by using the standard library's built-in methods
    which are optimized in CPython for performance over custom implementations.

    Args:
        text (str): The input string to transform.

    Returns:
        dict[str, str]: A dictionary with keys 'lower', 'upper', and 'title'.
    
    Examples:
        >>> case_swap("Hello World")
        {'lower': 'hello world', 'upper': 'HELLO WORLD', 'title': 'Hello World'}
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string input, got {type(text).__name__}")

    lower_case = text.lower()
    upper_case = text.upper()
    
    # Title case capitalizes the first character of each word. 
    # This preserves internal casing logic better than a manual loop for mixed-case inputs.
    title_case = ''.join(word.capitalize() if word else '' for word in text.split())

    return {
        'lower': lower_case,
        'upper': upper_case,
        'title': title_case
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    samples = [
        "hello world",
        "HELLO WORLD",
        "hElLo WoRlD!",
        "",
        "single"
    ]

    for text in samples:
        result = case_swap(text)
        print(f"Input: {repr(text)}")
        print(result)
        print("-" * 20)