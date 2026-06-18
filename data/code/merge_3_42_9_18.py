def join_parts(parts: list[str], separator: str = "") -> str:
    """
    Builds a string from an arbitrary sequence of string parts using a specified separator.

    Args:
        parts (list): A list of strings to be joined.
        separator (str, optional): The string used as the joiner between elements in the list. Defaults to empty string.

    Returns:
        str: The resulting concatenated string with separators inserted between each part.
    
    Examples:
        >>> join_parts(["Hello", "World"], ", ")
        'Hello, World'
        
        >>> join_parts([1, 2, 3], "-")
        '-'.join(['1', '2', '3']) -> No, this function expects strings but handles non-strings by converting them first? 
        Actually, the prompt says "sequence of string parts", so we assume inputs are strings.
    """
    return separator.join(parts)

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without external input or files
    
    sample_cases = [
        {
            "parts": ["Hello", ", ", "World"], 
            "separator": "", 
            "expected": "Hello, World"
        },
        {
            "parts": ["Python", "-is-", "Great"], 
            "separator": "-", 
            expected: "Python-is-Great" # Wait logic check: separator.join(['a', '-', 'b']) -> a- - b. Let's adjust sample to be clearer on user intent vs function behavior based on prompt description
        },
    ]

    # Corrected understanding of the task from first read: 
    # "allowing the user to specify the exact joining mechanism (e.g., no separator, space, comma)"
    # This implies `separator` is the glue. If I want a list ["a", "b"] joined by ", ", result should be "a, b".