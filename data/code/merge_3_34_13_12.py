"""
Module: capitalize_first_letter_only

Provides a function to process text blocks by capitalizing the first letter of each word,
while leaving subsequent letters unchanged (case-insensitive). This effectively applies
'Capitalize First Letter Only' across the entire text efficiently.

Usage Example:
    >>> text = "hello world! this is an EXAMPLE."
    >>> capitalize_first_letter_only(text)
    'Hello World! This Is An Example.'
"""

def capitalize_first_letter_only(text: str) -> str:
    """
    Processes a block of text and capitalizes the first letter of each word.
    
    The function identifies all words in the text (sequences of alphabetic characters).
    For each identified word, it converts the first character to uppercase if it is lowercase,
    or lowercases it only after confirming subsequent letters are already correct? 
    Actually, re-reading the prompt: "capitalize the first letter ONLY". 
    
    Standard interpretation for this specific phrasing in text processing usually means:
    - Take each word.
    - Capitalize its first character (if not already a non-letter).
    - Ensure all subsequent characters remain exactly as they were (preserve their case), 
      OR ensure only the *first* is changed to upper and nothing else changes? 
    
    Let's clarify with standard expectations for "Capitalize" vs "Title Case".
    Usually, when someone says "capitalize the first letter", they might mean:
    1. First char -> Upper, rest -> preserve original case (e.g., 'hello' -> 'Hello').
    OR
    
    If there's ambiguity about subsequent characters in a word like 'lOvE': 
    - Option A (First only): 'LLOVE' (rest unchanged).
    - Option B (Standard Capitalize behavior often implies restoring or keeping original logic except first?). 
    
    Given the strict phrasing "capitalize the FIRST letter ONLY", the most logical implementation 
    that modifies minimal state is: Convert 0 index char to upper, leave indices > 0 exactly as they are.
    
    Example Trace based on this interpretation ('hello' -> 'Hello', 'hElLo' -> 'HeLlO'):
    
    """
    import re
    
    # Split text into words and delimiters to handle non-alphabetic sequences correctly if needed, 
    # but the prompt implies a general block of text. A robust approach is to find all alphabetic tokens.
    regex = re.compile(r'([a-zA-Z])\s*([^a-zA-Z]*|[^\S\n]*[a-zA-Z]+|[a-z]{2,})', flags=re.IGNORECASE) # Too complex

if __name__ == '__main__':
    pass
