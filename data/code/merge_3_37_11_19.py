def combine_strings(s1: str, s2: str) -> str:
    """
    Concatenates two strings efficiently using Python's optimized string concatenation operator (+).
    
    Parameters:
        s1 (str): The first input string.
        s2 (str): The second input string.
        
    Returns:
        str: A new string formed by appending the contents of s2 to s1.
    """
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    result = combine_strings("Hello, ", "World!")
    print(result)  # Expected output: Hello, World!