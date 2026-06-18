def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the string character by character to identify words,
    yielding only the first alphabetic character found at the start of a new word.
    It avoids creating intermediate lists or strings for memory efficiency.

    Args:
        input_string (str): The string to process.

    Yields:
        str: A single-character string representing the first letter of a word, 
             if it is an alphabetic character. If no words are found or only non-alphabetic characters exist, nothing is yielded.
    
    Example:
        >>> list(find_first_letters_optimized("Hello world"))
        ['H', 'w']
    """
    in_word = False
    
    for char in input_string:
        if not in_word and ('A' <= char <= 'Z') or ('a' <= char <= 'y'):  # Check for alphabetic characters (excluding space)
            yield char
            in_word = True
        
        elif char == ' ':
            in_word = False

if __name__ == '__main__':
    sample_strings = [
        "Hello world",
        "Python is awesome!",
        "   Leading spaces here",
        "No words at all 123",
        ""
    ]
    
    for test_input in sample_strings:
        result = list(find_first_letters_optimized(test_input))
        print(f"Input: '{test_input}'")
        print(f"Output: {result}")
        print("-" * 40)