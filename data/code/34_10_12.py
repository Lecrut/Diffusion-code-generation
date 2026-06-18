#!/usr/bin/env python3
"""
Script to capitalize the first letter of each word in a string while preserving other casing.
Uses efficient string manipulation methods without external dependencies or user input.
"""

def capitalize_words(text: str) -> str:
    """
    Capitalizes only the first letter of each word, leaving the rest unchanged.

    Args:
        text (str): The input string to process.

    Returns:
        str: A new string with the first character of each word capitalized.
    """
    if not isinstance(text, str) or not text.strip():
        return ""

    result = []
    # Split by whitespace but keep track of original spacing for robustness
    parts = text.split()
    
    # Reconstruct preserving spaces between words (split without keeping separators loses them in simple split())
    # However, a more efficient approach using regex or manual iteration avoids creating intermediate lists if memory is tight.
    # Given the requirement for efficiency and simplicity: join capitalized first letters with original spacing logic.

    processed_words = []
    
    for word in parts:
        if not word:  # Handle multiple spaces as empty strings (though split() removes them by default)
            continue
            
        # Capitalize only the first character, leave the rest exactly as is
        new_word = word[0].upper() + word[1:] if len(word) > 1 else word[0]
        processed_words.append(new_word)

    return " ".join(processed_words)

def main():
    """
    Main execution block with hard-coded sample values.
    Runs without user input, command-line arguments, or network access.
    """
    
    # Sample inputs to test various cases: normal text, multiple spaces, mixed case preservation needed internally (though task says preserve rest of casing)
    samples = [
        "Hello World!",           # Standard sentence with punctuation attached
        "  Python   Programming", # Extra whitespace handling check if split() is used strictly on words
        "aBcDeFgHiJkLmNOpQrStUvWxYzZ", # Single word mixed case preservation
    ]

    for sample in samples:
        capitalized = capitalize_words(sample)
        print(f"Input:  '{sample}'")
        print(f"Output: '{capitalized}'\n")

if __name__ == '__main__':
    main()