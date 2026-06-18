#!/usr/bin/env python3
"""
Script to print the first letter of each word in a given string.
Handles various whitespace scenarios including multiple spaces, tabs, newlines, and mixed separators.
Operates efficiently on standard strings without external dependencies.
"""

def extract_first_letters(text: str) -> list[str]:
    """
    Extracts the first character from each non-empty sequence of characters (word).
    
    Args:
        text: Input string containing words separated by whitespace or other delimiters.
        
    Returns:
        A list of single-character strings representing the first letter of each word found in order.
    """
    result = []
    
    # Using a regex approach is efficient for tokenization, but to avoid external imports if not needed,
    # we can use string methods and iteration which are pure Python and very fast for this task.
    # We split the text by whitespace using .split() as it handles all types of whitespace (spaces, tabs, newlines) 
    # efficiently in CPython. This automatically filters out empty strings resulting from consecutive delimiters.
    
    words = text.split()
    
    if not words:
        return result
    
    for word in words:
        if len(word) > 0:
            first_letter = word[0]
            # Ensure it's a letter, though the prompt implies 'first letter of each word'. 
            # Usually words contain letters. If non-letter characters are at the start (e.g., hyphenated), 
            # strictly speaking, "letter" might imply alphabetic. However, standard definition treats any character in a token as part of it.
            # Given typical usage patterns for this task, we take index 0 regardless of case or type unless specified otherwise.
            result.append(first_letter)
            
    return result

def main():
    """
    Main execution block with hard-coded sample values.
    Tests the function on various inputs to demonstrate robustness against whitespace scenarios.
    """
    
    # Sample 1: Standard single spaces
    test_01 = "Hello World Python Programming"
    
    # Sample 2: Multiple consecutive spaces and tabs/newlines mixed
    test_02 = "Python\n\tIs   \nRobust!"
    
    # Sample 3: Leading/trailing whitespace
    test_03 = "  Start Here  End Now  "
    
    # Sample 4: Mixed punctuation attached to words (handled as part of the word by default split)
    test_04 = "--Code-- is --Fast."

    samples = [test_01, test_02, test_03, test_04]
    
    for i, sample_text in enumerate(samples):
        print(f"\n--- Input: {repr(sample_text)} ---")
        output_letters = extract_first_letters(sample_text)
        # Join and format for cleaner output display if needed, but printing individual letters is fine.
        result_string = ''.join(output_letters) or " (no words found)"
        print(result_string)

if __name__ == '__main__':
    main()