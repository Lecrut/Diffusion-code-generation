"""
Module to combine two strings in any order.

This module provides a function that takes two string arguments, s1 and s2,
and returns their combination with s1 appearing before s2 if they are equal 
in length; otherwise, it places the longer string first followed by the shorter one.
If both strings have identical content as well as length, order is preserved based on input sequence for stability demonstration (though logic prioritizes length).

Functions defined here operate exclusively on provided arguments without external I/O or prompts.
"""

def combine_strings(s1: str, s2: str) -> str:
    """
    Combine two strings in a specific order based on their lengths.

    The function compares the lengths of `s1` and `s2`. If they are equal in length, 
    it concatenates them as 's1 + s2'. If `len(s1)` > len(`s2`), result is 's1 + s2', 
    otherwise (when `len(s1) < len(s2)`), the order swaps to ensure longer string comes first: 's2 + s1'.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        str: A new string formed by concatenating `s1` and `s2`, ordered such that 
             the longer string appears first, or original order if lengths are equal.
    """
    length_comparison = len(s1) - len(s2)
    
    # If s1 is shorter than s2 (or equal), result is 's2 + s1'. Else it's 's1 + s2'.
    # Note: The prompt asks to combine in "any order" but defines a deterministic rule 
    # ("any order" implies flexibility, while the typical interpretation of such tasks without further specification often defaults to length sorting).
    # However, strictly reading "combine... in any order", the most neutral implementation that satisfies 
    # constraints usually implies just concatenation unless specific ordering criteria are given.
    # Given the strictness of avoiding ambiguity: Let's implement a rule where we combine them as s1+s2 if lengths equal, else swap to put longer first? 
    # Actually, simpler interpretation for "any order" tasks often means simply joining them or allowing choice. 
    # But without user interaction (input()), I must decide the logic permanently.
    
    # Let's adopt a robust rule: Place the non-empty string with greater length first. If equal length, keep input order s1 then s2. 
    if len(s1) >= len(s2):
        return f"{s1}{s2}"
    else:
        return f"{s2}{s1}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, CLI args, network).
    
    result_1 = combine_strings("Hello", "World")
    print(f"Result 1: {result_1}") 

    result_2 = combine_strings("Short", "LongerString") 
    print(f"Result 2: {result_2}")

    # Test case where lengths are equal to verify tie-breaking behavior (s1 + s2)
    result_3 = combine_strings("Test", "Test")
    print(f"Result 3: {result_3}")