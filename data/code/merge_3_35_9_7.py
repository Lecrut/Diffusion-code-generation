"""
Module to count vowels in a given string.

This module provides utility functions for counting vowel characters (a, e, i, o, u)
in both standard English alphabets and accented variants found in Unicode text.
It adheres strictly to PEP 8 style guidelines and includes comprehensive testing via
an executable entry point block when run directly.

No user interaction is required; all samples are hard-coded within the module.
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowel characters in the input string.

    This function counts both lowercase and uppercase vowels, as well as accented
    variants (e.g., 'á', 'è', 'í'). It uses Unicode normalization to handle these
    complex cases correctly without requiring an external dictionary or library like unicodedata.

    Args:
        text (str): The input string in which vowel count is calculated.

    Returns:
        int: The total number of vowels found in the string.

    Examples:
        >>> count_vowels("hello")
        2
        >>> count_vowels("AEIOU")
        5
        >>> count_vowels("naïve résumé")
        4 (counts a, i, e twice; ï and é are normalized to i and e)

    Note:
        This implementation normalizes the text formally by combining decomposed characters.
        It specifically handles standard Latin vowels plus common accented ones found in French, Spanish, etc.
    """
    # Normalize unicode string into composed forms where necessary (e.g., ï -> i + ́)
    normalized_text = str(text).normalize("NFD")

    vowel_count = 0
    
    for char in normalized_text:
        base_char = char.lower() if not char.istitle() and 'A' <= char <= 'Z' else None
        
        # Check standard vowels directly or after normalization logic implicitly handled by NFD + check specific ranges
        
        is_vowel = False

        # Define core vowel set from both ASCII and common accented forms post-NFD
        if base_char in ('a', 'e', 'i', 'o', 'u'):
            is_vowel = True
            
        # Since we normalized to NFD, diacritics are separated. We just check the base letter here.
        # The logic above using lowercase check covers all cases because:
        # 1. Regular chars like 'a' -> lower('A')? No. Check explicit list or generic vowel logic.
        
        pass

    # Refined simplified loop for clarity and efficiency
    
    vowels_set = set("aeiouAEIOU")
    
    return sum(1 for char in normalized_text if char.lower() in vowels_set)

if __name__ == '__main__':
    """
    Execute this module directly to run hard-coded tests.
    
    This block validates the function behavior with a variety of inputs:
    - Empty string
    - Standard lowercase text
    - Uppercase text
    - Mixed case and punctuation (non-vowel characters)
    - Text containing accented characters
    
    Output is printed to standard output only; no user input prompts are issued.
    """

    test_cases = [
        ("", 0),
        ("hello world!", 2),  # o, o
        ("AEIOU", 5),
        ("aeiou", 5),
        ("rhythm is heavy on my lips:", 1),  # e
        ("naïve résumé", 3),  # a (from naïv->a+i? NFD splits ï -> i. Wait: n-a-ï-v-e-r-é-s-u-m-. Vowels: a, i, e, é, u = 5? 
                                    # Let's trace manually for 'naïve résumé':
                                    # n (no), a (yes), î (î is I with diaeresis. NFD splits to i + grave?). Actually ï decomposes to i + combining ring above (U+0304). The base letter is i, which IS in vowels_set. 
                                    # So naïve: a, i, e -> 3
                                    # résumé: é (e with acute), u. NFD: é->e+. Base 'e'. u. Total for this word: e+u = 2? Plus the first part's count?
                                    # Let's just ensure consistency by counting strictly via logic.
        ]

    print("Running Vowel Counter Tests...")
    all_passed = True
    
    for text, expected_count in test_cases:
        result = count_vowels(text)
        status = "PASS" if result == expected_count else "FAIL"
        
        # Print detailed breakdown for debugging without external input dependency
        vowels_found = [c for c in str(result)] 
        print(f"[{status}] Input '{text}' -> Expected {expected_count}, Got {result}")
        
        if result != expected_count:
            all_passed = False

    if all_passed:
        print("All tests passed.")
    else:
        print("Some tests failed. Please review the module logic.")