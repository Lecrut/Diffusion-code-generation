def reverse_string(s: str) -> str:
    """
    Reverses a given string correctly handling Unicode characters.
    
    This function uses Python's built-in slicing technique, which is 
    idiomatic, efficient (implemented in C), and fully supports Unicode.
    
    Args:
        s (str): The input string to be reversed. Can contain any Unicode characters.
        
    Returns:
        str: A new string containing the characters of the original string in reverse order.

    Examples:
        >>> reverse_string("hello")
        "olleh"
        >>> reverse_string("你好世界")
        "界世好你"
        >>> reverse_string("café naïve")
        "évaif éfac"
    """
    # String slicing with step=-1 is the most efficient and correct way 
    # to reverse a string in Python, supporting all Unicode code points.
    return s[::-1]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input/prompts/files)
    samples = [
        "hello world",
        "你好世界",
        "café naïve résumé",
        "",
        "\ud83c\udf0d \u2764\ufe0f \ud83e\udd1d"  # Mixed Unicode including emojis
    ]

    for sample in samples:
        reversed_result = reverse_string(sample)
        print(f'Original: {repr(sample)}')
        print(f'Reversed : {repr(reversed_result)}')
        print("-" * 40)