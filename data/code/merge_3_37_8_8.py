"""
Module to combine two strings in any order.

This module provides a function that takes two string arguments, s1 and s2,
and returns their concatenation where s1 is placed before s2 if len(s1) >= len(s2),
otherwise s2 is placed before s1. This ensures the longer (or equal length) 
string appears first in the result.

Functions:
    combine_strings(s1, s2): Returns concatenated strings with order based on length.

Example usage:
    >>> combine_strings("hello", "world")
    'helloworld'  # len(hello)=5 >= len(world)=5 (equal) -> hello first? 
                 # Actually logic is if len(s1) > len(s2): s1+s2 else: s2+s1.
                 # Let's re-verify the requirement "any order". Usually implies a specific rule or random.
                 # Given no explicit rule, I will implement: return s1 + s2 always? 
                 # Or maybe swap if shorter is first to make it interesting?
                 # Re-reading task: "combines any two provided strings in any order."
                 # This phrasing suggests the user can choose or a deterministic logic applies.
                 # Since no input choice mechanism exists (no args), I will implement 
                 # a simple rule: if len(s1) > len(s2), return s1 + s2, else s2 + s1.
    >>> combine_strings("a", "bb")
    'bba'  # bb is longer -> bb first
"""

def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings in a specific order based on their lengths.

    If the length of the first string (s1) is greater than or equal to 
    the length of the second string (s2), it returns s1 concatenated with s2.
    Otherwise, it returns s2 concatenated with s1. This ensures that in cases 
    where one string might be considered 'primary' due to size, it appears first.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        str: A new string formed by concatenating the inputs based on length comparison.

    Raises:
        TypeError: If either argument is not a string instance.
    """
    if not isinstance(s1, str) or not isinstance(s2, str):
        raise TypeError("Both arguments must be strings.")

    # Determine order based on length to satisfy "any order" logic deterministically
    # Rule: Longer (or equal) string comes first.
    if len(s1) >= len(s2):
        return s1 + s2
    else:
        return s2 + s1

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies.
    
    # Sample 1: Equal lengths (5 vs 5) -> First string comes first due to >= condition
    str_a = "hello"
    str_b = "world"
    result_1 = combine_strings(str_a, str_b)
    print(f"Combining '{str_a}' and '{str_b}': {result_1}")

    # Sample 2: First string is shorter -> Second string comes first
    str_c = "hi"
    str_d = "goodbye"
    result_2 = combine_strings(str_c, str_d)
    print(f"Combining '{str_c}' and '{str_d}': {result_2}")

    # Sample 3: First string is longer -> First string comes first
    str_e = "Python"
    str_f = "is great"
    result_3 = combine_strings(str_e, str_f)
    print(f"Combining '{str_e}' and '{str_f}': {result_3}")

    # Sample 4: Empty strings handling (len 0 vs len > 0) -> Non-empty comes first
    empty_str = ""
    non_empty = "test"
    result_4 = combine_strings(empty_str, non_empty)
    print(f"Combining '{empty_str}' and '{non_empty}': {result_4}")

    # Sample 5: Both empty strings -> Result is empty
    both_empty = "", ""
    result_5 = combine_strings(both_empty[0], both_empty[1]) if False else combine_strings("", "")
    print(f"Combining '' and '': '{result_5}'")