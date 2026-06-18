def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the string character by character to identify 
    words and yield their starting letters, ensuring minimal memory usage 
    without storing intermediate lists or sets.

    Args:
        input_string (str): The string containing multiple words separated by whitespace.
        
    Yields:
        str: A single-character string representing the first letter of each word found.
    
    Example:
        >>> list(find_first_letters_optimized("Hello world"))
        ['H', 'w']
    """
    # Initialize a flag to track if we are currently inside a new word
    in_word = False
    
    for char in input_string:
        is_alpha = ('a' <= char.lower() <= 'z') or ('A' <= char.upper() <= 'Z')
        
        # If the character is alphabetic and not already in a word, it's the start of one
        if is_alpha and not in_word:
            yield char
            in_word = True
        
        # Update state for next iteration (if we are inside a word, continue tracking)
        elif is_alpha:
            pass  # Continue processing as part of the current word

# Main execution block with hard-coded sample values to ensure no external dependencies or input required.
if __name__ == '__main__':
    test_cases = [
        "Hello world",
        "Python programming language",
        "",
        "   Multiple spaces between words here  ",
        "SingleWord"
    ]

    for text in test_cases:
        result_list = list(find_first_letters_optimized(text))
        print(f'Input: "{text}"')
        print(f'Result: {result_list}')
        print()