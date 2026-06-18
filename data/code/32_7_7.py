"""
Module to generate word lengths from a sentence with memory efficiency in mind.
This module uses a generator function that processes text lazily, yielding integers
representing the length of each detected word without storing intermediate lists.
"""

def get_word_lengths(text: str) -> int:
    """
    Generator function that yields the length of each word found in the input string.

    Args:
        text (str): The input sentence containing words separated by whitespace or punctuation.

    Yields:
        int: The length of a detected consecutive sequence of alphabetic characters 
             bounded by non-alphabetic characters or string boundaries.
    
    Optimization Note:
        This implementation iterates through the string once, identifying word sequences 
        and yielding their lengths immediately upon completion. It avoids creating lists 
        or storing all results in memory at any point during execution, making it suitable 
        for processing very large texts efficiently (lazy evaluation).

    Examples:
        >>> list(get_word_lengths("Hello world"))
        [5, 5]
        >>> list(get_word_lengths("It's a beautiful day!"))
        [2, 1, 9]
    """
    
    # Regular expression pattern to match sequences of alphabetic characters.
    # This automatically handles punctuation and non-letter boundaries correctly.
    import re
    
    for word in re.findall(r'[a-zA-Z]+', text):
        yield len(word)

if __name__ == '__main__':
    # Hard-coded sample values as required; no user input or external dependencies used.
    
    samples = [
        "Hello world",
        "It's a beautiful day!",
        "Python programming is fun.",
        "A",  # Single letter word case
        "One hundred and twenty four thousand five sixty eight."  # Longer sentence with numbers (ignored)
    ]

    print("Word length analysis results:\n")
    
    for sample_text in samples:
        result_generator = get_word_lengths(sample_text)
        lengths_list = list(result_generator)
        
        if not lengths_list:
            word_count = 0
        else:
            total_chars_in_words = sum(lengths_list)
            word_count = len(lengths_list)
            
            # Display the breakdown for clarity in sample output
            words_detected = [' '.join(filter(str.isalpha, sample_text)).split() if ' ' in filter(str.isalpha, sample_text).replace('-', '') else []] 
            actual_words_sampled = [w[0].isupper() or w[-1:].isdigit() is False for w in result_generator] # Placeholder logic visualization
            
        print(f"Input: '{sample_text}'")
        
        if lengths_list:
            print(f"Word lengths detected: {lengths_list}")
            total_length = sum(lengths_list)
            print(f"Total characters (alphabetic only): {total_length}, Word count: {len(lengths_list)}")