def reverse_string(s: str) -> str:
    """
    Reverses the order of characters in a given string, handling Unicode correctly.
    
    This function iterates over the input string from end to start and constructs 
    a new string with the characters in reversed order. It properly handles all 
    valid Unicode scalar values (including emojis, accented letters, etc.) because 
    Python 3 strings are sequences of code points by default when accessed via iteration
    or slicing operations on str objects directly without explicit unicode handling flags.

    Parameters:
        s (str): The input string to be reversed. Can contain any Unicode characters.

    Returns:
        str: A new string containing the characters of the original string in reverse order.
    
    Example:
        >>> reverse_string("Hello, 世界!")
        '!界世，olleH'
    """
    return s[::-1]

if __name__ == '__main__':
    # Sample values to test without user input or external dependencies
    sample_inputs = [
        "Python is great",
        "Unicode: 🌍🚀✨",
        "",
        "Single character 'a'",
        "Café résumé naïve"
    ]

    for text in sample_inputs:
        reversed_text = reverse_string(text)
        print(f"Original: {text!r}")
        print(f"Reversed:{reversed_text!r}\n")