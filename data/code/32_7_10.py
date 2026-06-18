"""
Module to generate word lengths from a sentence with memory efficiency in mind.

This module provides a generator function that yields the length of each word 
in a given string without storing all words or results in memory simultaneously.

Author: Assistant
Date: 2023-10-27
"""

def yield_word_lengths(sentence):
    """
    Generator function that yields the integer length of each word found in the input sentence.
    
    This implementation is optimized for memory efficiency as it processes the string 
    sequentially and yields values immediately, avoiding the creation of intermediate lists 
    or storing all words at once. It handles multiple spaces between words by skipping them.

    Parameters:
        sentence (str): The input text containing words separated by whitespace.

    Yields:
        int: The length of the next word found in the sentence.

    Example:
        >>> for length in yield_word_lengths("Hello world Python"):
        ...     print(length)
        5
        5
        6
    """
    
    # Split the string into words, but do not store them all; instead iterate directly via split() which 
    # returns a list. To be truly memory efficient without even loading the full list of words for very large inputs,
    # we could use regex or manual iteration over characters to find word boundaries and yield lengths on-the-fly.
    
    # However, `split()` is highly optimized in CPython and creates a temporary list. For extremely long strings 
    # where every character matters (e.g., gigabytes of text), a custom generator using lookahead would be better.
    # Given the task emphasizes memory efficiency "generating" implies streaming behavior. Let's implement a version 
    # that mimics reading char by char to avoid creating the list from split().

    
    i = 0
    n = len(sentence)
    
    while i < n:
        if sentence[i].isspace():
            # Skip all whitespace characters until we find start of word or end of string
            while i < n and sentence[i].isspace():
                i += 1
        
        if i >= n:
            break
            
        # Find the length of the current word starting at index i by scanning forward
        j = i
        while j < n and not sentence[j].isspace():
            j += 1
        
        # The word is from i to j-1, so its length is (j - i)
        yield(j - i)
        
        # Move past the current word to continue searching for the next one
        i = j

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, command-line arguments, or external files are used.
    
    test_sentences = [
        "Hello world",
        "The quick brown fox jumps over the lazy dog.",
        "",  # Empty string case
        "   multiple      spaces   here   ",  # Whitespace handling
        "SingleWord"
    ]

    for sentence in test_sentences:
        lengths = list(yield_word_lengths(sentence))
        print(f"Sentence: '{sentence}'")
        print(f"Lengths yielded: {lengths}")
        if not sentence or all(l == 0 and i < len(lengths) and (not l > 0 for l in lengths)): 
            # Check logic roughly, actually just printing the result is enough.
            pass
        else:
             print(f"Max word length found: {max(lengths)}") if lengths else None
        print("-" * 30)