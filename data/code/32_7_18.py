import re

def get_word_lengths(sentence: str):
    """
    Generator function that yields the length of each word in a sentence.
    
    Args:
        sentence (str): The input string containing words separated by whitespace or punctuation.
        
    Yields:
        int: The integer representing the number of characters in each extracted word.
    
    This implementation optimizes for memory efficiency by processing the text 
    as an iterator and yielding values immediately, without creating intermediate lists.
    """
    # Use a regex to find all sequences of alphanumeric characters (words)
    # \b ensures we match whole words only
    for match in re.finditer(r'\w+', sentence):
        word = match.group()
        yield len(word)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or external access is used here.
    test_sentences = [
        "The quick brown fox jumps over the lazy dog",
        "One 234! Hello... world?? end.",
        "Python programming languages are powerful and efficient."
    ]

    # Process each sample sentence to demonstrate functionality
    for s in test_sentences:
        print(f"Input string: {s}")
        
        # Convert generator to list immediately just for display purposes 
        lengths_list = list(get_word_lengths(s))
        
        print(f"Word lengths (list): {lengths_list}")
        
        # Also demonstrate usage as a true generator in memory-efficient scenarios
        
        length_sum_generator = get_word_lengths(s)
        total_length = sum(length_sum_generator)  # Consumes the generator once