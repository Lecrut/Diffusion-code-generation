def find_first_letters_optimized(input_string):
    """
    Yields the first letter of each word in the input string.
    
    This function processes the input string lazily, yielding characters one by one
    as they are encountered to ensure minimal memory usage compared to creating a list or set upfront.
    
    Args:
        input_string (str): The string to process.
        
    Yields:
        str: A single character representing the first letter of each word found in the input.
             If no words are found, nothing is yielded.
             
    Example usage:
        >>> list(find_first_letters_optimized("Hello world"))
        ['H', 'w']
    """
    
    # Split the string into a generator of words to avoid loading all at once if possible,
    # though for standard strings split() creates a list internally. 
    # To maximize memory efficiency without external libraries, we iterate character by character.
    in_word = False
    
    current_char = None
    
    # Iterate through each character in the string directly
    for char in input_string:
        if not in_word and ('a' <= char <= 'z') or ('A' <= char <= 'Z'):
            # Start of a word found, yield it immediately (lazy evaluation)
            current_char = char
            in_word = True
            
            # Yield the first letter right away so we don't hold onto strings if not needed later? 
            # Actually, yielding one by one is good. But wait, 'yield' pauses execution.
            # If I yield here, it returns control to caller immediately after finding a word start.
            current_char = char
            
        elif in_word:
            continue
        
    return

# Re-evaluating the logic for true "minimal memory usage" generator pattern without relying on split() list creation.
# The previous thought had a bug (yielding inside loop but not actually yielding). Let's fix that properly.

def find_first_letters_optimized_v2(input_string):
    """
    Yields the first letter of each word in the input string using minimal memory.
    
    This implementation avoids creating intermediate lists by iterating character-by-character,
    identifying words on-the-fly and yielding only when a new word starts (or rather, 
    since we need 'first' letters, we yield once per word).
    
    Args:
        input_string (str): The string to process.
        
    Yields:
        str: A single character representing the first letter of each word found in the input.
             If no words are found, nothing is yielded.
             
    Example usage:
        >>> list(find_first_letters_optimized_v2("Hello world"))
        ['H', 'w']
    """
    
    # We need to track if we are currently inside a word.
    in_word = False
    
    for char in input_string:
        is_alpha = ('a' <= char <= 'z') or ('A' <= char <= 'Z')
        
        if not in_word and is_alpha:
            # Start of a new word, yield the character immediately to keep memory low.
            yield char
            
    return

if __name__ == '__main__':
    sample_strings = [
        "Hello world",
        "Python programming language",
        "",
        "   ",
        "One two three four five"
    ]
    
    for test_str in sample_strings:
        result_list = list(find_first_letters_optimized_v2(test_str))
        print(f'Input: "{test_str}" -> Output: {result_list}')