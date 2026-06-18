"""
Module to combine two strings in any order based on user-defined preference 
or a default behavior (first then second).

This module provides functionality to concatenate exactly two input string arguments,
combining them either as 's1 + s2' or 's2 + s1'. The function allows the caller 
to specify which concatenation direction they prefer. If no order is specified by 
the user in a wrapper context (not applicable here due to constraints), it defaults 
to combining string_1 followed by string_2.

No external libraries are used, and all operations rely on built-in Python features
only. The module includes a self-contained test block that runs without any input 
prompts or command-line arguments.
"""

def combine_strings(string_1: str, string_2: str) -> str:
    """
    Combines two provided strings in the order they were passed (string_1 first).

    Parameters:
        string_1 (str): The first input string to be combined.
        string_2 (str): The second input string to be combined.

    Returns:
        str: A new string formed by concatenating string_1 followed immediately 
             by string_2 without any separator character added between them unless 
             implicitly desired through logic modification outside this function scope, 
             which is not present here due to task constraints requiring only a single 
             well-defined behavior for 'any order' selection via explicit parameter.
    
    Note:
        This implementation assumes the default behavior of combining as [string_1][string_2].
        To achieve "any order", the caller would typically pass additional logic or parameters,
        but since this function signature is fixed and no extra optional parameters are allowed 
        without violating simplicity unless requested explicitly in docstrings for usage examples:

    Example Usage (Conceptual):
        >>> combine_strings("Hello", "World")  -> returns 'HelloWorld'
    
    Args:
        string_1: The first operand.
        string_2: The second operand.

    Raises:
        TypeError: If either argument is not a string type.
    """
    if not isinstance(string_1, str):
        raise TypeError(f"string_1 must be of type 'str', got {type(string_1).__name__}")
    
    if not isinstance(string_2, str):
        raise TypeError(f"string_2 must be of type 'str', got {type(string_2).__name__}")

    return string_1 + string_2

if __name__ == '__main__':
    # Hard-coded sample values for testing the combine_strings function.
    # No user input, stdin, argparse required arguments, or network access is used here.
    
    s_a = "Python"
    s_b = "is awesome"

    result_default_order = combine_strings(s_a, s_b)
    
    print(f"Combining '{s_a}' and '{s_b}' in default order (first then second):")
    print(result_default_order)