def combine_strings(str1: str, str2: str) -> str:
    """Combines two input strings into a single string separated by a space."""
    if not isinstance(str1, str):
        raise TypeError(f"Expected 'str' for first argument, got {type(str1).__name__}")
    if not isinstance(str2, str):
        raise TypeError(f"Expected 'str' for second argument, got {type(str2).__name__}")
    
    return f"{str1} {str2}"

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    str_a = "Python"
    str_b = "is_awesome"

    result = combine_strings(str_a, str_b)
    
    print(result)