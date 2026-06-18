#!/usr/bin/env python3
"""
Script to identify repeated letters in a given string.
This script operates on lowercase alphabetic characters, ignoring case during matching but preserving original casing context if needed (though output is normalized).
Non-alphabetic characters are skipped for the purpose of repetition detection.

Author: AI Assistant
Date: 2023-10-07
"""

def find_repeated_letters(text: str) -> list[str]:
    """
    Analyzes a string to find letters that appear more than once.
    
    Parameters:
        text (str): The input string to analyze.
        
    Returns:
        list[str]: A sorted list of unique repeated characters found in the string,
                   converted to lowercase for consistent output.
                    
    Raises:
        TypeError: If the input is not a string.
    """
    
    # Validate input type
    if not isinstance(text, str):
        raise TypeError("Input must be a string.")

    letter_counts = {}

    # Iterate through each character in the text
    for char in text:
        # Check if the character is an alphabetic letter
        if 'a' <= char.lower() <= 'z':
            # Convert to lowercase and update count
            lower_char = char.lower()
            if lower_char not in letter_counts:
                letter_counts[lower_char] = 0
            
            letter_counts[lower_char] += 1

    # Identify letters with a frequency greater than one
    repeated_letters = [char for char, count in letter_counts.items() if count > 1]

    return sorted(repeated_letters)

if __name__ == '__main__':
    sample_1 = "Hello World!"
    sample_2 = "Programming is Fun and Great"
    
    # Process first sample
    result_1 = find_repeated_letters(sample_1)
    print(f"Input: '{sample_1}'")
    if not result_1:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters (case-insensitive): {', '.join(result_1)}")

    # Process second sample
    result_2 = find_repeated_letters(sample_2)
    print("\nInput: '{sample_2}'".format(sample_2=sample_2)) 
    if not result_2:
        print("No repeated letters found.")
    else:
        print(f"Repeated letters (case-insensitive): {', '.join(result_2)}")