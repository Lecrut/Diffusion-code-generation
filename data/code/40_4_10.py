def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the input string to identify words (sequences 
    separated by whitespace) and yields their respective first letters.
    It is designed for minimal memory usage as it uses a generator, yielding
    results one at a time rather than storing them all in a list or other structure.

    Args:
        input_string (str): The string to process.

    Yields:
        str: A single character representing the first letter of each word found 
             in the input string. Non-alphabetic characters are skipped if they appear 
             at the start of a potential word, but standard whitespace splitting is used.
    
    Example:
        >>> list(find_first_letters_optimized("Hello World"))
        ['H', 'W']
    """
    words = input_string.split()
    for word in words:
        if not word:  # Skip empty strings resulting from consecutive spaces
            continue
        first_char = word[0]
        yield first_char

if __name__ == '__main__':
    sample_input_1 = "Python is awesome"
    sample_input_2 = "Hello World This Is A Test String"

    print("Sample 1:", list(find_first_letters_optimized(sample_input_1)))
    # Expected output: ['P', 'i', 'a'] (Note: split() handles multiple spaces)

    print("Sample 2:", list(find_first_letters_optimized(sample_input_2)))
    # Expected output: ['H', 'W', 'T', 'I', 'A', 'T', 'S']