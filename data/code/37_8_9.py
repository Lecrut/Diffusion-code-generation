"""
Module to combine two strings in any order based on a specified rule.

This module provides functionality to concatenate two input strings either 
in their original order or with positions swapped, depending on an optional parameter.

Author: AI Assistant
Date: 2023-10-27
Version: 1.0.0
"""

def combine_strings(str_a: str, str_b: str, reverse_order: bool = False) -> str:
    """
    Combines two strings in a specified order.

    Args:
        str_a (str): The first string to be combined.
        str_b (str): The second string to be combined.
        reverse_order (bool): If True, combines as 'b' + 'a'. 
                             If False, combines as 'a' + 'b'.

    Returns:
        str: The resulting concatenated string based on the order parameter.

    Examples:
        >>> combine_strings("Hello", "World")
        'HelloWorld'
        >>> combine_strings("Python", "Code", reverse_order=True)
        'CodePython'
    """
    if not isinstance(str_a, str):
        raise TypeError(f"Expected string for str_a, got {type(str_a)}")
    if not isinstance(str_b, str):
        raise TypeError(f"Expected string for str_b, got {type(str_b)}")

    return f"{str_b}{str_a}" if reverse_order else f"{str_a}{str_b}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    sample_string_1 = "Alice"
    sample_string_2 = "Bob"

    result_normal = combine_strings(sample_string_1, sample_string_2)
    result_reversed = combine_strings(sample_string_2, sample_string_1, reverse_order=True)

    print(f"Normal Order ({sample_string_1} + {sample_string_2}):")
    print(result_normal)

    print("\nReversed Order:")
    print(result_reversed)