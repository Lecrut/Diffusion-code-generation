#!/usr/bin/env python3
"""
Script to calculate the total character length of a given string,
including spaces and punctuation. This script accepts input via hardcoded samples 
and prints the result without any interactive prompts or external dependencies.
"""

def count_characters(text: str) -> int:
    """
    Returns the total number of characters in the provided text string.
    
    Args:
        text (str): The input string to analyze.
        
    Returns:
        int: The length of the string, including all characters such as spaces and punctuation.
    """
    return len(text)

def main():
    # Hard-coded sample values for testing purposes without user interaction
    samples = [
        "Hello World",
        "!@#$%^&*()",
        "",  # Edge case: empty string
        "Python is awesome!",
        "   Multiple spaces here. ",
    ]

    print("Character Length Calculator")
    print("-" * 30)

    for sample in samples:
        character_count = count_characters(sample)
        original_string = repr(sample).strip("'\"") if len(repr(sample)) > 2 else repr(sample)
        
        # Using a simple check to determine if the string is empty based on its representation length, 
        # or just directly use the sample itself for display logic.
        display_str = "Empty" if not sample else f'"{sample}"'

        print(f'Sample: {display_str}')
        print(f'Total Characters (including spaces & punctuation): {character_count}\n')

if __name__ == '__main__':
    main()