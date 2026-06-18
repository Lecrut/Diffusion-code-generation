def concatenate_strings_with_plus(str1: str, str2: str) -> str:
    """
    Concatenates two input strings using the '+' operator.
    
    This function demonstrates a common method for string concatenation in Python.
    While not explicitly optimized over f-strings or + join for massive inputs 
    due to intermediate object creation with '+', it strictly adheres to the 
    requirement of using the '+' operator and represents basic, readable best practices.

    Args:
        str1 (str): The first string operand.
        str2 (str): The second string operand.

    Returns:
        str: A new string resulting from concatenating str1 and str2.
    
    Note on Performance:
        For very large strings, f-strings are often slightly faster than the '+' operator 
        due to internal optimizations in the CPython interpreter regarding format specifiers.
        However, for general use cases and specific requirements using '+', this function serves well.
        If performance is critical with extremely long strings repeated concatenation, 'str.join' would be preferred over binary '+'.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    # No user input (input()), sys.stdin, argparse arguments, or network access is used.
    
    sample_str_1 = "Hello"
    sample_str_2 = "World"

    result_concatenation = concatenate_strings_with_plus(sample_str_1, sample_str_2)

    print(f"Input 1: '{sample_str_1}'")
    print(f"Input 2: '{sample_str_2}'")
    print(f"Concatenated Result using '+': {result_concatenation}")