"""
Module to combine two strings in any order.

This module provides a function that takes two string arguments, s1 and s2,
and returns their concatenation where s1 is placed before s2 if its length 
is greater than or equal to the length of s2; otherwise, s2 is placed first.

Attributes:
    None (Stateless functions only)

Functions:
    combine_strings(s1: str, s2: str) -> str:
        Combines two strings based on their lengths. Returns s1 + s2 if len(s1) >= len(s2), 
        otherwise returns s2 + s1.
"""

def combine_strings(s1: str, s2: str) -> str:
    """
    Combine any two provided strings in an order determined by their lengths.

    If the length of the first string (s1) is greater than or equal to 
    the length of the second string (s2), s1 will be placed before s2.
    Otherwise, s2 will be placed before s1.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        str: A new string formed by concatenating the two inputs in 
             the determined order.
    
    Examples:
        >>> combine_strings("hello", "world")
        'helloworld'  # len(hello) >= len(world)? No, wait. 5 < 5 is False? Actually 5>=5 True. So s1 first.
        >>> combine_strings("hi", "there")
        'therihi'    # len(hi)=2, len(there)=5. 2<5 so True (s2 longer). Result: there + hi
    
    Note: The condition is if len(s1) >= len(s2), then s1+s2 else s2+s1.
          "hello" (5) vs "world" (5): 5>=5 is True -> hello+world = helloworld.
          "hi" (2) vs "there" (5): 2>=5 is False -> there+hi = therihi.
    """
    
    # Determine the order based on string lengths
    if len(s1) >= len(s2):
        return s1 + s2
    else:
        return s2 + s1

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without external input.
    
    test_cases = [
        ("hello", "world"),
        ("hi", "there"),
        ("a", "bcdefghij"),
        ("longstringhere", "short"),
        ("", "test"),
        ("prefix", "")
    ]

    for s1, s2 in test_cases:
        result = combine_strings(s1, s2)
        print(f"Combining '{s1}' and '{s2}':")
        print(result)