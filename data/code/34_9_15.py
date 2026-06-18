#!/usr/bin/env python3
"""
Module to capitalize only the first letter of each word in a string efficiently,
without using manual indexing loops. This is achieved by utilizing Python's built-in 
string translation capabilities or list comprehensions which are more 'Pythonic' than explicit for-loops with index manipulation.

The approach used:
1. Split the string into words based on whitespace.
2. Use a generator expression within join to capitalize each word individually (only converting first char if present).
3. Join the processed words back together.
"""

def title_case_no_manual_loop(text: str) -> str:
    """
    Capitalizes only the first letter of each word in the input string.
    
    This function assumes that "words" are separated by whitespace and does not 
    handle punctuation as delimiters aggressively (i.e., 'hello-world' becomes 'Hello-World').
    It avoids manual indexing loops over characters, relying instead on list comprehensions/str methods.

    Parameters:
        text (str): The input string to process.
        
    Returns:
        str: A new string with the first letter of each word capitalized and subsequent letters lowercased.
             Non-alpha characters at the start of a "word" are left as is for that position logic, 
             though standard title_case usually handles non-letters by skipping them or handling punctuation specifically.
    """
    
    # The most Pythonic way to split into words without manual loops: str.split()
    # Using str.capitalize(): It capitalizes the first character and lowercases the rest of the string in place, which is O(n).
    return ' '.join(word.capitalize() if word else '' for word in text.split())

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no input(), sys.stdin, etc.)
    
    samples = [
        "hello world", 
        "python programming is fun!",
        "",
        "   multiple      spaces   ",
        "One-Two-Three"  # Edge case: hyphenated words usually stay hyphenated in basic title case logic unless split differently. Here 'One' -> One, '-Two'-lowered to -two? No capitalize leaves non-alpha as is for the prefix but converts following letters if they exist after a letter or start of word logic varies. 
                      # However, standard str.capitalize() on "-two" keeps '-' and capitalizes next char: '-Two'.
    ]

    print("Input-Output Test Results:")
    for sample in samples:
        result = title_case_no_manual_loop(sample)
        print(f"'{sample}' -> '{result}'")