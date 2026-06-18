"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which 
characters appear more than once, and returns them sorted alphabetically (or by ASCII value).
It utilizes Python's built-in 'set' data structure for efficient duplicate detection.

Usage:
    Run the script directly to see results on hard-coded sample strings.
"""

def find_repeated_characters(text: str) -> list[str]:
    """
    Detects and lists all characters that appear more than once in the given string.
    
    The function uses set operations to determine unique elements first, then iterates 
    through the original text to identify which of those unique elements occur multiple times.
    
    Args:
        text (str): The input string to analyze for repeated characters.
        
    Returns:
        list[str]: A sorted list of unique characters that are repeated in the input string.
                   If no repetitions exist, returns an empty list.
                   
    Example:
        >>> find_repeated_characters("hello world")
        ['d', 'e', 'h', 'l', 'o']
        
    Note:
        The result is sorted based on ASCII values (uppercase letters come before lowercase).
    """
    
    # Convert the string to a set of unique characters for O(1) lookup.
    unique_chars = set(text)
    
    repeated_chars = []
    
    # Iterate over each character in the original text.
    for char in text:
        count_text = 0
        
        # Count occurrences of this specific character in the entire string.
        for c in text:
            if c == char:
                count_text += 1
                
        # If a character appears more than once, add it to our result list only if 
        # it hasn't been added yet (to avoid duplicates in the output list).
        if count_text > 1 and char not in repeated_chars:
            repeated_chars.append(char)
            
    return sorted(repeated_chars)

def main():
    """
    Main execution block. Runs with hard-coded sample values to demonstrate functionality
    without requiring user input, command-line arguments, or external resources.
    
    This function calls find_repeated_characters on several test cases including 
    mixed case strings, special characters (where supported by the environment), and empty inputs.
    """
    
    # Sample 1: Basic repeated letters in a sentence
    sample_1 = "programming is fun"
    
    # Sample 2: String with uppercase and lowercase duplicates
    sample_2 = "AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz"
    
    # Sample 3: String with no repeated characters (prime-like sequence of chars)
    sample_3 = "abcdefg"
    
    # Sample 4: Empty string edge case
    sample_4 = ""
    
    test_cases = [sample_1, sample_2, sample_3, sample_4]
    
    print("Repeated Character Detection Results")
    print("=" * 50)
    
    for idx, text in enumerate(test_cases):
        result = find_repeated_characters(text)
        
        # Display input string (truncated if too long for readability)
        display_text = text[:20] + "..." if len(text) > 20 else text
        
        print(f"\nTest Case {idx + 1}:")
        print(f"Input:    '{display_text}'")
        
        # Handle empty result specifically for clarity
        if not result:
            print("Repeated characters found: None")
        else:
            print(f"Repeated chars (sorted): {result}")

if __name__ == '__main__':
    main()