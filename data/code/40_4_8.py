def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word found in the input string.
    
    This function processes the string character by character to identify words 
    without converting the entire string into a list, ensuring minimal memory usage.
    A 'word' is defined as a sequence of non-whitespace characters (as opposed to split(), which creates new objects).

    Args:
        input_string (str): The string to process.

    Yields:
        str: The first character of each word found in the input string. 
             If no words are found, nothing is yielded.
    
    Example usage within main block: list(find_first_letters_optimized("Hello World")) -> ['H', 'W']
    """
    # Flag to track if we have seen a non-whitespace character (start of a word)
    first_letter_set = False
    
    for char in input_string:
        # Check if the current character is not whitespace and it marks the start of a new sequence
        if char.isalpha(): 
            yield char
            
def main_if_block():
    """
    Main execution block containing hard-coded sample values.
    This ensures no user input, command-line arguments, or external dependencies are required.
    """
    
    # Sample 1: Basic string with multiple words and punctuation
    sample_1 = "The quick brown fox jumps over the lazy dog."
    
    # Sample 2: String starting with numbers but containing letters later ("4" is not a letter, 'h' in four? No, we only want letters)
    # The prompt asks for first letter. If input is "abc123", words are likely based on whitespace or just sequences of non-space chars? 
    # Usually "first letter of each word". Let's assume standard definition: sequence of alphanumeric/symbol as a token if separated by space, but strictly taking the FIRST LETTER (isalpha).
    sample_2 = "Hello World 123" 
    
    # Sample 3: String with only whitespace or no letters
    sample_3 = "\t\n   \n\tabc def"

    print("Processing:", repr(sample_1))
    result_set_1 = set()

if __name__ == '__main__':
    pass
