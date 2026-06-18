"""
Module to combine two strings in any order.

This module provides a function that takes two string arguments and returns 
a new string formed by concatenating them in either 'string1 + string2' or 
'string2 + string1'. The user can choose the desired order via boolean flag 
or simply rely on default behavior which is s1 then s2.
"""

def combine_strings(s1: str, s2: str) -> tuple[str, str]:
    """
    Combines two provided strings in any order and returns both possible results.

    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.

    Returns:
        tuple[str, str]: A tuple containing the concatenation of s1+s2 followed by s2+s1.
    
    Example:
        >>> combine_strings("Hello", "World")
        ('HelloWorld', 'WorldHello')
    """
    result_order_1 = f"{s1}{s2}"
    result_order_2 = f"{s2}{s1}"
    return result_order_1, result_order_2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    str_a = "Python"
    str_b = "is awesome"

    combined_first, combined_second = combine_strings(str_a, str_b)

    print(f"Order 1 ({str_a} + {str_b}): '{combined_first}'")
    print(f"Order 2 ({str_b} + {str_a}): '{combined_second}'")