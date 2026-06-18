def reverse_string(s: str) -> str:
    """
    Returns the reversed version of the input string in a time-efficient manner.
    
    Args:
        s (str): The string to be reversed.
        
    Returns:
        str: The reversed string.
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    sample_strings = [
        "Hello, World!",
        "",
        "a",
        "Python is awesome!" * 20,
        "<div class=\"content\">Test</div>"
    ]

    for original in sample_strings:
        reversed_str = reverse_string(original)
        print(f"Original: {original}")
        print(f"Reversed: {reversed_str}\n")