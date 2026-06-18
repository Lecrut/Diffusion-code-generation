def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the input string efficiently by using a generator,
    which ensures minimal memory usage as it does not create intermediate lists or strings.
    It iterates through the characters and identifies words based on whitespace delimiters.

    Args:
        input_string (str): The string to process.

    Yields:
        str: A single character representing the first letter of a word, 
             if one exists in that segment.
    
    Example Usage:
        >>> list(find_first_letters_optimized("Hello World"))
        ['H', 'W']
    """
    current_word = ""
    
    for char in input_string:
        # Check if the character is a letter (alphabetic)
        if char.isalpha():
            current_word += char
            
            # If we have accumulated at least one letter, yield it immediately.
            # This ensures minimal memory usage by not storing all results until needed.
            if len(current_word) == 1:
                yield char
        
        else:
            # Reset the word accumulator on encountering non-letter characters (like spaces).
            current_word = ""

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies.
    samples = [
        "Hello World",
        "Python Programming is Fun!",
        "",
        "   Multiple   Spaces  Here ",
        "SingleWord"
    ]

    for test_input in samples:
        result_list = list(find_first_letters_optimized(test_input))
        print(f"Input: '{test_input}'")
        print(f"Output: {result_list}")
        print("-" * 20)