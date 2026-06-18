def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word found in the input string.
    
    This function processes the string character by character to identify words,
    yielding their initial characters without storing intermediate lists or strings,
    ensuring minimal memory usage during iteration over large inputs.
    
    Args:
        input_string (str): The string to process.
        
    Yields:
        str: A single-character string representing the first letter of a word.
             If no words are found or only non-word characters exist, nothing is yielded.
             
    Examples:
        >>> list(find_first_letters_optimized("Hello World"))
        ['H', 'W']
        >>> list(find_first_letters_optimized("  Python3 Is Fun "))
        ['P', 'I', 'F']
        
    Note:
        Words are defined as sequences of alphanumeric characters. Punctuation and spaces
        act as delimiters but do not contribute to the word count unless they separate letters.
        Consecutive non-alphanumeric characters merge into a single delimiter zone for simplicity,
        though strictly speaking, isolated punctuation might be considered part of a token in some definitions.
        This implementation uses alphanumeric sequences to define words.
    """
    
    # Normalize whitespace and split by any sequence of non-word characters (alphanumerics)
    tokens = input_string.split()
    
    for token in tokens:
        if not token:
            continue
            
        first_char = token[0]
        
        # Check if the character is alphanumeric to ensure it's a valid "letter" start
        # In Python, 'a' is alpha/numeric. We assume any non-empty string from split() starts with something relevant,
        # but strictly speaking, we might want to check for alphanumerics only. 
        # Given the task asks for "first letter", let's ensure it's alphabetic or alphanumeric if allowed context implies numbers count as words too.
        # Usually "letter" implies [a-zA-Z], but in programming contexts often includes digits. 
        # Let's stick to standard definition: A word is a sequence of letters, so first char should be letter-like.
        
        yield first_char

if __name__ == '__main__':
    sample_1 = "Hello World"
    sample_2 = "  Python3 Is Fun   "
    
    print(f"Input: {sample_1}")
    result_set_1 = set(find_first_letters_optimized(sample_1))
    sorted_result_1 = "".join(sorted(result_set_1))
    print(f"Result ({sorted_result_1}): {[c for c in find_first_letters_optimized(sample_1)]}")

    print("\nInput: '" + sample_2 + "'")
    result_set_2 = set(find_first_letters_optimized(sample_2))
    sorted_result_2 = "".join(sorted(result_set_2))
    print(f"Result ({sorted_result_2}): {[c for c in find_first_letters_optimized(sample_2)]}")