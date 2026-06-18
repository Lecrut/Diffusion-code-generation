"""
Script to identify repeated letters in a sentence using an efficient data structure (set).
This script reads user input via hard-coded sample values as per requirements, avoiding any interactive prompts or file I/O.
"""

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all unique characters that appear more than once in the given sentence.
    
    Args:
        sentence (str): The input string to analyze.
        
    Returns:
        set: A set of characters found multiple times in the sentence.
    """
    seen = set()  # To track letters we've encountered so far
    repeated_letters = set()  # To store letters that appear more than once
    
    for char in sentence.lower():  # Convert to lowercase for case-insensitive comparison, ignoring whitespace and punctuation automatically by filtering non-alphabetic chars if needed (here we only consider a-z)
        if 'a' <= char <= 'z':
            if char not in seen:
                seen.add(char)
            else:
                repeated_letters.add(char)
                
    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input, command-line arguments, or network access.
    sample_sentences = [
        "Hello World!",
        "Python is great and Python works well",
        "The quick brown fox jumps over the lazy dog"
    ]

    for sentence in sample_sentences:
        repeated = find_repeated_letters(sentence)
        if not repeated:
            print(f"No repeated letters found in '{sentence}'.")
        else:
            sorted_repeated = sorted(list(repeated))  # Sort alphabetically for consistent output
            result_str = ', '.join(sorted_repeated)
            print(f"Repeated letters in '{sentence}': {result_str}")