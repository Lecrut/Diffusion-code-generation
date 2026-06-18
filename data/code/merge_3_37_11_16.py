def combine_strings(s1: str, s2: str) -> str:
    """
    Concatenates two strings efficiently using Python's + operator or f-string formatting.
    
    Args:
        s1 (str): The first string argument.
        s2 (str): The second string argument.
        
    Returns:
        str: A new string formed by concatenating s1 and s2.
    """
    return s1 + s2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    result = combine_strings("Hello", "World")
    print(result)  # Output: HelloWorld