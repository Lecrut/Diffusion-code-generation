"""
Performance-focused solution to capitalize the first letter of a string.
Handles edge cases: empty strings, strings with no letters, 
strings starting with punctuation (only capitalizes if it's actually alphabetic).

Time Complexity: O(n) where n is the length of the input string.
Space Complexity: O(1) auxiliary space as we operate in-place or create a new list/tuple efficiently.
"""

def capitalize_first_letter(s: str) -> str:
    """
    Capitalizes only the first alphabetic character found in the string, 
    leaving all other characters unchanged (including case).

    Args:
        s (str): The input string to process.

    Returns:
        str: A new string with the first letter capitalized if it exists and is a letter.
             If no letters exist or the string is empty, returns the original string.
    """
    # Handle empty strings immediately for efficiency
    if not s:
        return ""
    
    result_list = []
    
    # Iterate through characters to find the first alphabetic character
    i = 0
    while i < len(s) and (not s[i].isalpha()):
        result_list.append(s[i])
        i += 1
    
    # If no letter was found, return original string as per requirements ("only" if exists)
    # However, standard interpretation of "capitalize first letter" implies if no letter, 
    # do nothing. Let's stick to strict logic: capitalize ONLY the FIRST LETTER.
    
    if i < len(s):
        # Found a letter at index i, capitalize it and append rest as is
        result_list.append(s[i].upper())
        
        for char in s[i+1:]:
            result_list.append(char)
    else:
        # No alphabetic character found in the entire string
        return "".join(result_list)

    return "".join(result_list)

if __name__ == '__main':
    # Hard-coded sample values covering edge cases and typical usage.
    test_cases = [
        "",                        # Empty string
        "hello",                   # Normal case
        "  world!",               # Leading punctuation/spaces
        "123abc",                 # Numbers then letter
        "!@#$%",                  # No letters at all
        "aBcDeFgHiJkLmNOpQrStUvWxYz",  # Multiple letters (only first should be changed)
        "",                       # Double empty check
    ]

    print("Input\tOutput")
    for test in test_cases:
        output = capitalize_first_letter(test)
        print(f"{repr(test)}\t{repr(output)}")

if __name__ == '__main__':
    pass
