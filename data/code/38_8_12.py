"""
Module to detect and list all repeated characters in an input string using set operations.

This module provides a function that takes a string as input, identifies which 
characters appear more than once, and returns them sorted by their first occurrence order 
to maintain intuitive grouping based on the text flow. It uses Python's built-in `set`
data structure for efficient duplicate detection (O(n) time complexity).

The module is designed to run standalone without requiring user input, command-line arguments,
network access, or pre-existing files.
"""

def find_repeated_characters(text: str) -> list[str]:
    """
    Identifies all characters that appear more than once in the provided string.
    
    The function iterates through each unique character found in the text. 
    It counts its occurrences and collects those with a count greater than 1, 
    preserving their original order of appearance in the input string.

    Args:
        text (str): The input string to analyze for repeated characters.

    Returns:
        list[str]: A sorted list of unique characters that are repeated in the input string.

    Example:
        >>> find_repeated_characters("hello world")
        ['l', 'o']  # Note: order depends on first appearance logic, here l and o appear twice
        
        Actually based on standard set iteration order or custom ordering: 
        Let's ensure we return them in the order they *first* appeared.
    """
    
    char_counts = {}
    repeated_chars_ordered = []

    # First pass: Count occurrences of each character while tracking first appearance index if needed,
    # but simpler logic is to just count all, then filter and sort by original position.
    for char in text:
        char_counts[char] = char_counts.get(char, 0) + 1
    
    # Second pass: Build the list of repeated characters ordered by their first appearance index
    seen_indices_map = {} 
    # We need to track which indices we've already included a character at (the first one)
    
    for idx, char in enumerate(text):
        if char_counts[char] > 1 and char not in seen_indices_map:
            repeated_chars_ordered.append(char)
            seen_indices_map[char] = True
            
    return repeated_chars_ordered

def main():
    """
    Main execution block. Runs with hard-coded sample values to demonstrate functionality.
    
    This section does not require user input, command-line arguments, or network access.
    It demonstrates the behavior of find_repeated_characters on a few predefined strings.
    """

    # Sample inputs for testing
    test_strings = [
        "hello world",      # 'l' and 'o' are repeated (ignoring case sensitivity as per standard set usage unless specified)
        "aabbccddeeffggghhhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzzz",  # All letters except one if any, here all pairs repeat. Wait: a,a b,b ... z,z -> all repeated. Let's use specific ones.
        "Python Programming is fun!", # ' ', 'i', 'm' (if case insensitive? Task implies standard char manipulation usually case-sensitive unless stated otherwise). 
                                      # Standard interpretation: Case sensitive. 'P','y','t','h','o','n',' ','P','r','o','g','r','a','m'ming'...
    ]

    print("Repeated Characters Detector")
    print("-" * 30)

    for test_str in test_strings:
        repeated = find_repeated_characters(test_str)
        
        # Format output nicely, showing the character and its count if desired, 
        # but strictly returning/listing characters as per task "list all repeated characters".
        char_list_repr = "".join(reversed(repeated))  # Just to show them together
        
        print(f"Input: '{test_str}'")
        print(f"Repeated Characters (in order of appearance): {repeated}")
        
        if not any(c in ' \n\t' for c in repeated): 
            # Optional: skip whitespace from list? No, task says "characters". Whitespace is a character.
            pass
            
    print("-" * 30)

if __name__ == '__main__':
    main()