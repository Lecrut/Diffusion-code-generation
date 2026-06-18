#!/usr/bin/env python3
"""Script to reverse a string character by character."""

def main():
    """Main function containing hardcoded test cases with no user input required."""
    
    # Sample inputs without requiring any external data or user prompts
    sample_strings = [
        "Hello, World!",
        "", 
        "a",           # Edge case: single character
        "!@#$%",       # Special characters
        "Python 3.9"   # Space included
    ]

    for original in sample_strings:
        reversed_string = original[::-1]
        print(f"Original: '{original}'")
        print(f"Reversed: '{reversed_string}'\n")

if __name__ == '__main__':
    main()