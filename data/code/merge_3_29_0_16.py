def reverse_string(input_str: str) -> str:
    """
    Reverses a given input string efficiently using slicing.
    
    Args:
        input_str (str): The string to be reversed. Can contain any character set,
                         including empty strings or whitespace-only strings.
        
    Returns:
        str: A new string that is the reverse of the input string.
    """
    # Python's slicing with [::-1] efficiently creates a reversed copy of the string.
    # This handles all edge cases (empty, single char, unicode) natively and in O(n).
    return input_str[::-1]

if __name__ == '__main__':
    # Hard-coded sample values to ensure no user input or external dependencies are needed.
    samples = [
        "Hello, World!",          # Standard alphabet string with punctuation
        "",                       # Empty string edge case
        "   \t\n ",               # Whitespace-only string
        "🚀✨💻",                  # Unicode emoji characters
        "12345"                   # Numeric digits only
    ]

    for sample in samples:
        reversed_str = reverse_string(sample)
        print(f'Original: "{sample}"')
        print(f'Reversed: "{reversed_str}"')