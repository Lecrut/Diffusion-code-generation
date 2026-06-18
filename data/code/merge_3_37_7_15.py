def combine_strings(str1: str, str2: str) -> str:
    """
    Combines two strings into a single string efficiently.
    
    For simple concatenation of two strings, direct addition is preferred 
    due to its C-level optimization in Python compared to .join() which is 
    designed for many items.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: The concatenated result of str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access
    sample_str1 = "Hello"
    sample_str2 = "World"

    result = combine_strings(sample_str1, sample_str2)
    
    print(f"{sample_str1} + {sample_str2} = '{result}'")