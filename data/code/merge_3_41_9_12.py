def case_swap(text: str) -> dict:
    """
    Returns a dictionary mapping 'lower', 'upper', and 'title' to their respective 
    case transformations of the input string.

    Args:
        text (str): The input string to transform.

    Returns:
        dict: A dictionary with keys 'lower', 'upper', and 'title'.
              - 'lower': All characters converted to lowercase.
              - 'upper': All characters converted to uppercase.
              - 'title': First character capitalized, rest lowercased (standard title case).
    
    Example:
        >>> result = case_swap("hello world")
        # returns {'lower': 'hello world', 'upper': 'HELLO WORLD', 'title': 'Hello World'}
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected string input, got {type(text).__name__}")

    lower_result = text.lower()
    upper_result = text.upper()
    
    # Standard title case: capitalize first letter of each word found by splitting on whitespace
    words = text.split()
    if not words:
        title_result = ""
    else:
        capitalized_words = [word.capitalize() for word in words]
        title_result = " ".join(capitalized_words)

    return {
        'lower': lower_result,
        'upper': upper_result,
        'title': title_result
    }

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    samples = [
        "hello world",
        "PYTHON IS FUN",
        "  leading spaces and trailing spaces ",
        "",
        "mixed CASE 123"
    ]

    print("Case Transformation Results:")
    for text in samples:
        result = case_swap(text)
        print(f"\nInput: '{text}'")
        print(f"Lower: '{result['lower']}'")
        print(f"Upper: '{result['upper']}'")
        print(f"title : '{result['title']}'")