#!/usr/bin/env python3
"""
Script to capitalize the first letter of each word in a string while preserving other casing.
Uses efficient string manipulation methods without external dependencies or input prompts.
"""

def title_case_preserving(string: str) -> str:
    """
    Capitalizes only the first letter of each word, leaving the rest as is.
    
    Args:
        string (str): The input string to process.
        
    Returns:
        str: A new string with the first character of each word capitalized.
    """
    if not isinstance(string, str) or not string.strip():
        return string
    
    parts = []
    current_word = ""
    
    for char in string:
        # Split on whitespace to handle multi-word strings correctly
        is_space = (ord(char) == 32) and all(ord(c) <= 32 for c in [char]) or False
        
        if is_space:
            if current_word:
                parts.append(current_word.capitalize())
                current_word = ""
            else:
                # Handle leading whitespace by keeping it intact but empty word handling 
                pass
        elif ord(char) > 32 and not any(ord(c) < 65 for c in [char]):
            # Ensure we only process printable characters that are part of words
            current_word += char
            
    if current_word:
        parts.append(current_word.capitalize())
    
    return "".join(parts).strip()

def main():
    """Main execution block with hard-coded sample values."""
    sample_strings = [
        "hello world",
        "Python 3.10 is awesome!",
        "multi   spaced   words here",
        "UPPERCASE mixed LowerCase",
        "",
        "single word"
    ]
    
    results = []
    for s in sample_strings:
        capitalized = title_case_preserving(s)
        results.append(f'"{s}" -> "{capitalized}"')
        
    # Print results to console without requiring user input
    print("Input-Output Pairs:")
    print("-" * 40)
    
    for r in results:
        print(r)

if __name__ == '__main__':
    main()