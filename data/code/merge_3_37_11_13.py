def combine_strings(str1: str, str2: str) -> str:
    """
    Concatenates two strings efficiently using Python's native string concatenation.
    
    In modern CPython implementations (3.x), the + operator for strings is optimized 
    to create a new string object with minimal overhead compared to manual character loops.
    This method leverages that optimization directly.

    Args:
        str1 (str): The first input string.
        str2 (str): The second input string.

    Returns:
        str: A new string formed by concatenating str1 and str2.
    """
    return str1 + str2

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    result = combine_strings("Hello", "World")
    print(result)  # Expected output: HelloWorld