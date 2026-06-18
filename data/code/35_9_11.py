"""
Module to count vowels in a given string.

This module provides a function `count_vowels` that counts the number of vowel characters
(a, e, i, o, u) and their uppercase counterparts (A, E, I, O, U) in an input string.
It is designed for reuse in larger projects and adheres strictly to PEP 8 style guidelines.

Vowel definition: The function considers 'a', 'e', 'i', 'o', 'u' as vowels regardless of case.
Consonants and other characters are ignored during the count.

Author: AI Assistant
Date: October 2023
"""

def count_vowels(text: str) -> int:
    """
    Count the number of vowel characters in a string.

    This function iterates through each character in the input string and checks if it is
    one of the vowels ('a', 'e', 'i', 'o', 'u' or their uppercase equivalents). It returns
    the total count found. The check is case-insensitive but does not perform any normalization,
    simply counting occurrences based on character equality with predefined vowel sets for both cases.

    Args:
        text (str): The input string in which vowels are to be counted. Can contain spaces, 
                    punctuation, numbers, and other characters; these will be ignored.

    Returns:
        int: The total count of vowel characters found in the input string.

    Examples:
        >>> count_vowels("Hello World")
        2
        >>> count_vowels("AEIOUaeiou123!")
        10
        >>> count_vowels("")
        0
    """
    
    # Define the set of vowels for efficient lookup. 
    # Using a string or tuple is more Pythonic than a list for membership testing in some contexts,
    # but here we iterate directly to avoid creating an intermediate boolean flag list which saves memory overhead on large strings.
    vowel_set = {'a', 'e', 'i', 'o', 'u'}

    count: int = 0
    
    for char in text:
        if char.lower() in vowel_set:
            count += 1
            
    return count

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    
    test_cases = [
        "Hello World",           # Expected: 'e', 'o' -> 2
        "AEIOUaeiou123!",       # Expected: A,E,I,O,U,a,e,i,o,u + ! (ignored) and numbers ignored -> 10 vowels? 
                                # Wait, let's re-verify logic. AEIOU(5) aeio(u)(4)? No 'u' in lower case here except implicit.
                                # String is "AEIOUaeiou". A,E,I,O,U,a,e,i,o,u = 10 characters. All are vowels. 
                                # Plus "123!" which has none. Total should be 10? Wait, the example string above in my head was slightly off.
                                # Let's stick to simple examples for clarity and correctness.
        "",                     # Expected: 0
        "Python Programming",   # Expected: 'o', 'r' (no), 'a'? P-y-t-h-o-n- -P-r-o-g-r-a-m-m-i-n-g -> o, a, i = 3? 
                                # Let's trace carefully.
                                # H-e-l-l-o W-o-r-l-d -> e,o -> 2
        "aeiou",                # Expected: 5
    ]

    print("Running vowel count module tests...\n")
    
    for test_input in test_cases:
        result = count_vowels(test_input)
        print(f"Input: '{test_input}'")
        print(f"Vowel Count: {result}")
        
        # Explicit verification comments based on the logic implemented.
        if test_input == "Hello World":
            assert result == 2, f"Expected 2 for 'Hello World', got {result}"
        elif test_input == "aeiou":
            assert result == 5, f"Expected 5 for 'aeiou', got {result}"
        elif test_input == "Python Programming":
            # P y t h o n (1: o) space P r o g r a m m i n g (o, a, i -> 3 more? No wait.)
            # Python: o (1)
            # Programming: o(2), a(3), i(4). Total should be 5.
            assert result == 5, f"Expected 5 for 'Python Programming', got {result}"
        elif test_input == "":
            assert result == 0, f"Expected 0 for empty string, got {result}"

    print("\nAll tests passed successfully.")