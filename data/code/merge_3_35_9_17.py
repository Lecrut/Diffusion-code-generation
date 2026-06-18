"""
Module to count vowels in a given string.

This module provides a function `count_vowels` that counts the number of vowel characters
(a, e, i, o, u) and their uppercase counterparts (A, E, I, O, U) in an input string.
The counting is case-insensitive but treats non-vowel letters as ignored regardless of case.

Usage:
    from count_vowels import count_vowels
    
    text = "Hello World"
    result = count_vowels(text)  # Returns 3 (e, o, o)
"""

def count_vowels(input_string: str) -> int:
    """
    Count the number of vowel characters in a string.

    This function iterates through each character in the input string and checks if it is
    one of the vowels ('a', 'e', 'i', 'o', 'u' or their uppercase equivalents). It returns
    the total count found. Non-alphabetic characters are ignored without raising errors.

    Args:
        input_string (str): The string in which to count vowels. Can contain any type of 
                            character, including spaces and symbols.

    Returns:
        int: The number of vowel characters present in the input string.

    Examples:
        >>> count_vowels("aeiou")
        5
        >>> count_vowels("")
        0
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("Rhythm is sweet!")
        2 (i, e)

    Note:
        This implementation does not use regular expressions to avoid potential performance 
        overhead in very large strings. It uses a simple set lookup for O(1) average time 
        complexity per character check.
    
    Raises:
        TypeError: If input_string is not of type str (though Python's dynamic typing usually 
                  prevents this at runtime, explicit checks are good practice).

    """
    if not isinstance(input_string, str):
        raise TypeError(f"Expected string type, got {type(input_string).__name__}")

    vowels = {'a', 'e', 'i', 'o', 'u'}
    
    count = 0
    
    for char in input_string:
        lower_char = char.lower()
        if lower_char in vowels:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction.
    
    test_cases = [
        "Hello World",           # Expected: 3 (e, o, o)
        "",                      # Expected: 0
        "AEIOU",                 # Expected: 5
        "Rhythm is sweet!",     # Expected: 2 (i, e)
        "Python Programming",   # Expected: 4 (y-i-o-a -> y is not vowel here, i,o,a,e? Wait. P-y-t-h-o-n-P-r-o-g-r-a-m-m-i-n-g. o,n,r,o,g,r,a,m,i,n,g. Vowels: o, o, a, i. Total 4.)
        "12345",                 # Expected: 0 (no vowels)
    ]

    print("Vowel Count Test Results:")
    for test_input in test_cases:
        result = count_vowels(test_input)
        expected_count = sum(1 for c in test_input if c.lower() in {'a', 'e', 'i', 'o', 'u'})
        
        status = "PASS" if result == expected_count else "FAIL"
        print(f"Input: '{test_input}'")
        print(f"Counted Vowels: {result}")
        print(f"Expected Count: {expected_count} | Status: {status}\n")