#!/usr/bin/env python3
"""
Script to extract the first letter of each word from a given string.
Handles various whitespace scenarios including multiple spaces, tabs, newlines, 
and leading/trailing whitespaces efficiently using Python's built-in split() method.
"""

def get_first_letters(text: str) -> list[str]:
    """
    Returns a list containing the first letter of each word found in the input string.

    Args:
        text (str): The input string to process.

    Returns:
        list[str]: A list of single-character strings representing the first letters 
                   of each non-empty sequence of alphabetic characters. If no words are found,
                   an empty list is returned. Words are defined as sequences separated by whitespace.
    
    Example:
        >>> get_first_letters("  Hello   World! ")
        ['H', 'W']
    """
    # split() without arguments handles all types of whitespace (spaces, tabs, newlines) 
    # and automatically strips leading/trailing whitespace from the result list.
    words = text.split()

    first_letters = []
    
    for word in words:
        if not word:  # Safety check, though split() guarantees non-empty strings
            continue
        
        char_index = 0
        while char_index < len(word) and not word[char_index].isalpha():
            char_index += 1
            
        if char_index == 0 or (char_index > 0 and not word[char_index].isalpha()):
            # If the first character is not alphabetic, we skip it to find an actual letter.
            # However, based on standard "first letter" interpretation for mixed text:
            # We usually take the very first non-whitespace char if it's a letter, 
            # or potentially just the first char of the word regardless of case/type unless specified otherwise.
            # The prompt implies 'letter', so we look for an alphabetic character at the start.
            
            # Let's refine: If the user wants "first letter", they likely mean A-Z/a-z.
            # We scan from index 0 to find the first alpha char.
            pass

        if word[char_index].isalpha():
            first_letters.append(word[char_index])
    
    return first_letters

def get_first_letter_simple(text: str) -> list[str]:
    """
    Alternative implementation focusing strictly on the first character of each whitespace-separated token,
    assuming tokens are words. If a token starts with non-alphabetic characters (like punctuation), 
    this version might include them depending on strictness. 
    
    To be robust for "first letter", we should find the first alphabetic char in the word if it exists at index 0 or later.
    """
    words = text.split()
    result = []

    for word in words:
        # Find the first alphabetic character in this word
        found_alpha_index = -1
        
        # Iterate through characters to find an alpha one
        for i, char in enumerate(word):
            if char.isalpha():
                found_alpha_index = i
                break
        
        # If we found a letter within the word (even not at index 0), take it. 
        # Otherwise, skip this token as it has no letters.
        if found_alpha_index != -1:
            result.append(word[found_alpha_index])

    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    
    test_cases = [
        "  Hello   World! ",           # Multiple spaces, punctuation at end
        "\t\tPython\nis\nfun",         # Tabs and newlines mixed
        "--- --- -",                   # Only hyphens (no letters) -> empty result expected based on logic finding alpha
        "a b c d e f g h i j k l m n o p q r s t u v w x y z",  # Single chars separated by space
        "",                            # Empty string
        "   ",                         # Only whitespace
    ]

    print("First letters of each word:")
    
    for test_input in test_cases:
        output = get_first_letter_simple(test_input)
        
        if not output:
            print(f'Input: "{test_input}" -> Result: []')
        else:
            # Join with space or comma for readability, but the core logic returns a list. 
            # Printing as joined string is clearer than raw list repr in console usually.
            result_str = "".join(output) if len(output) > 1 else output[0]
            
            print(f'Input: "{test_input}" -> Result: {result_str}')

    # Explicit demonstration of the function call with a specific example from the block above
    sample_text = "The quick brown fox jumps over the lazy dog."
    final_result = get_first_letter_simple(sample_text)
    
    if not final_result:
        print(f"Sample '{sample_text}' -> No letters found.")
    else:
        joined_output = "".join(final_result)
        print(f"\nDetailed Sample Output for: \"{sample_text}\"")
        print(f"First Letters List: {final_result}")
        print(f"Joined String: \"{joined_output}\"")