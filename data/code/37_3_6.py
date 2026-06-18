def combine_strings(s1: str, s2: str) -> str:
    """
    Combines two input strings using the '+' operator.
    
    While Python optimizes string concatenation internally (e.g., via PyPy's vectorization or CPython's optimization for repeated operations), 
    direct usage of the '+' operator remains clear and idiomatic for simple combinations. 
    For performance-critical loops, join() is preferred; however, this function strictly adheres to the requirement of using '+'.
    
    Args:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: The concatenated result of s1 and s2.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_string_1 = "Hello, World!"
    sample_string_2 = "Python"
    
    result = combine_strings(sample_string_1, sample_string_2)
    print(f"{sample_string_1} + {sample_string_2} = '{result}'")