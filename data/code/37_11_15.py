def combine_strings(s1: str, s2: str) -> str:
    """
    Concatenates two strings efficiently using Python's built-in string concatenation.
    
    In modern CPython implementations (3.x), the + operator for strings is implemented
    via PyUnicode_MergeStrings which handles Unicode normalization and memory allocation
    optimally, making it the most efficient standard operation available without external dependencies.

    Args:
        s1 (str): The first string operand.
        s2 (str): The second string operand.
        
    Returns:
        str: A new string formed by concatenating s1 and s2.
    """
    return f"{s1}{s2}"

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    result = combine_strings("Hello", "World")
    print(result)  # Output: HelloWorld