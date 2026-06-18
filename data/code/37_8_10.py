"""
Module to combine two strings in any order.

This module provides a function that takes two string arguments, s1 and s2,
and returns their concatenation where s1 is placed before s2 if len(s1) >= len(s2),
otherwise s2 is placed before s1. This ensures the longer (or equal length) 
string appears first in the result.

The function handles empty strings correctly by treating them as having zero length,
which will cause any non-empty string to be prioritized based on its own content logic
if lengths were different, but since one is 0 and other > 0, the non-zero takes precedence.
If both are empty, it returns an empty string regardless of order.

No external libraries or interactive input methods are used.
"""

def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two strings in any order based on their lengths.
    
    The function determines the order by comparing the length of the first string (s1)
    with the second string (s2). If len(s1) is greater than or equal to len(s2), 
    s1 + s2 is returned; otherwise, s2 + s1 is returned. This ensures that strings 
    of equal length are combined as [first_arg] followed by [second_arg], while 
    longer strings take precedence over shorter ones in the output order.
    
    Args:
        s1 (str): The first input string to be combined.
        s2 (str): The second input string to be combined.
        
    Returns:
        str: A new string formed by concatenating either 's1 + s2' or 's2 + s1'.

    Examples:
        >>> combine_strings("hello", "world")
        'helloworld'  # len('hello') >= len('world') is False (5 < 5)? No, equal. So first arg wins? 
                     # Wait, logic check: if len(s1) >= len(s2): s1+s2 else s2+s1
                     # "hello" (5), "world" (5). 5>=5 True -> 'helloworld'. Correct per spec interpretation above.
        >>> combine_strings("a", "bb")
        'bba'         # len('a')=1, len('bb')=2. 1 >= 2 False -> s2+s1 = 'bba'.
    """
    
    if len(s1) >= len(s2):
        return f"{s1}{s2}"
    else:
        return f"{s2}{s1}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    str_a = "Python"
    str_b = "is awesome"

    result = combine_strings(str_a, str_b)
    
    print(f"Combining '{str_a}' and '{str_b}':")
    print(result)