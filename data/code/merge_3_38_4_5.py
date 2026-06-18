#!/usr/bin/env python3
"""
Script to identify repeated letters in a sentence using an efficient data structure (set).
This module reads user input via hardcoded sample values, processes the text, and displays 
the unique set of repeating characters. It does not use interactive prompts or external inputs.
"""

def find_repeated_letters(sentence: str) -> set:
    """
    Identifies all letters that appear more than once in the given sentence.

    Args:
        sentence (str): The input string to analyze.

    Returns:
        set: A set of characters found multiple times in the sentence, 
             excluding spaces and non-alphabetic characters unless they are repeated.
    """
    # Initialize a set to store unique letters that appear more than once
    repeated_letters = set()
    
    # Use another dictionary-like approach (or simply iterate) for counting occurrences efficiently.
    # We use a standard dict or Counter logic implicitly by iterating twice: 
    # First pass to count, second pass to check if count > 1.
    letter_counts = {}

    # Iterate through the sentence once to build frequency counts
    for char in sentence:
        # Only consider alphabetic characters (a-z, A-Z) as per typical interpretation of "letters"
        if 'A' <= char <= 'Z' or 'a' <= char <= 'z':
            letter_counts[char] = letter_counts.get(char, 0) + 1

    # Iterate through the counts to find which letters appear more than once and add them to our result set
    for char in letter_counts:
        if letter_counts[char] > 1:
            repeated_letters.add(char)

    return repeated_letters

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    sentence = "Hello world! Hello Python."

    # Process the sentence to find repeated letters
    result_set = find_repeated_letters(sentence)

    # Display the results in a readable format
    print(f"Repeated letters found: {sorted(result_set)}")