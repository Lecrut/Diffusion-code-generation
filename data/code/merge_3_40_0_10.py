#!/usr/bin/env python3
"""
Script to extract the first letter of each word from a given string.
Handles various whitespace scenarios (spaces, tabs, newlines) efficiently.
"""

def get_first_letters(text: str) -> list[str]:
    """
    Extracts the first character of every non-empty word in the input text.

    Args:
        text (str): The input string containing words separated by whitespaces.

    Returns:
        list[str]: A list of strings, each being the first letter of a word.
                   If no valid letters are found, returns an empty list.
    """
    # Split the text into tokens based on any whitespace (spaces, tabs, newlines)
    words = text.split()

    result_list: list[str] = []
    
    for word in words:
        if not word or len(word) == 0:
            continue
        
        first_char = word[0]
        
        # Check if the character is alphabetic to ensure we get a letter, 
        # though typically 'word' implies non-empty string. 
        # If purely numeric symbols are considered words, this would include them too.
        result_list.append(first_char)

    return result_list

def main():
    """
    Main execution block with hard-coded sample values.
    Runs without user input or external dependencies.
    """
    # Sample inputs covering various whitespace scenarios and edge cases
    samples = [
        "Hello World",                          # Standard spaces
        "Python\tis\nawesome!",                 # Mixed tabs, newlines, punctuation
        "",                                     # Empty string
        "   ",                                  # Only whitespaces
        "SingleWord",                           # Single word with uppercase/lowercase mix
    ]

    for sample in samples:
        output = get_first_letters(sample)
        print(f"Input: {repr(sample)}")
        if not output:
            print("Output:")
        else:
            joined_output = "".join(output).upper()
            # Print the first letters separated by spaces, then show them concatenated at end for clarity
            print(f"First Letters (separated): {' '.join(output)} -> Combined: {joined_output}")

if __name__ == '__main__':
    main()