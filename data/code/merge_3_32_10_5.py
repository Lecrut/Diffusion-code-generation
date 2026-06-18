def calculate_total_length(text):
    """
    Calculates the total character length of a given string.
    Includes spaces, punctuation, special characters, etc.
    
    Args:
        text (str): The input string to measure.
        
    Returns:
        int: The number of characters in the string.
    """
    return len(text)

if __name__ == '__main__':
    sample_strings = [
        "Hello, World!",  # Contains uppercase, lowercase, punctuation
        "",               # Empty string edge case
        "   ",            # String with only spaces
        "Python scripting is fun!"  # Mixed content example
    ]

    for s in sample_strings:
        length = calculate_total_length(s)
        print(f"Input: '{s}'")
        print(f"Total character count (including spaces and punctuation): {length}")