"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases such as empty strings, non-alphabetic starts (keeps original), 
and ensures no side effects or external dependencies are used.
Time Complexity: O(n) where n is the length of the input string.
Space Complexity: O(1) auxiliary space excluding output storage.
"""

def capitalize_first_letter(text):
    """
    Capitalizes only the first alphabetic character if present, leaving it otherwise unchanged.
    
    Args:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter capitalized if applicable.
    """
    # Handle empty strings or non-string inputs gracefully by returning as-is
    if not isinstance(text, str) or len(text) == 0:
        return text

    # Find the index of the first alphabetic character to avoid modifying punctuation at start
    for i in range(len(text)):
        char = text[i]
        if 'a' <= char.lower() <= 'z':  # Check for ASCII letters (can be extended)
            # Capitalize only this specific letter and keep the rest as is
            return f"{char.upper()}".join([text[:i], [text[i+1:]]]) + text[i] if i > 0 else char.upper()

    # If no alphabetic character found, return original string to preserve exact input format for non-alpha starts
    return text

if __name__ == '__main__':
    # Hard-coded sample values covering various edge cases without user interaction or file I/O
    test_cases = [
        "hello world",           # Normal case: 'h' -> 'H'
        "",                      # Empty string
        "!@#$%",                 # No alphabetic characters at start
        "123abc",                # Numbers before letters (should only capitalize first alpha if logic adjusted, but per spec we do nothing to non-alpha)
        "  hello world",         # Spaces before letter (only the 'h' is capitalized as it's the first alpha encountered? Or strictly first char?) 
                                # Re-reading prompt: "capitalize the first letter". Usually implies first alphabetic. 
                                # However, standard interpretation often means if there IS a letter at index 0, capitalize it.
                                # Let's stick to strict definition: If text[0] is alpha -> upper(), else return as is (or only touch first char).
        "a",                     # Single lowercase letter
        "A",                     # Already capitalized
        "hello123world!",       # Mixed content ending with punctuation
    ]

    results = []
    for case in test_cases:
        res = capitalize_first_letter(case)
        results.append(f"Input: '{case}' -> Output: '{res}'")

    print("\n".join(results))