def calculate_phrase_length(phrase: str) -> int:
    """
    Calculate the length of a given string (phrase).
    
    This function is optimized by directly returning len(), which is implemented 
    in C and provides O(n) time complexity with minimal overhead. It adheres 
    to Python best practices for simplicity, readability, and performance.

    Args:
        phrase (str): The input string whose length needs to be calculated.

    Returns:
        int: The number of characters in the provided string.
    
    Examples:
        >>> calculate_phrase_length("Hello")
        5
        >>> calculate_phrase_length("")
        0
    """
    return len(phrase)

if __name__ == '__main__':
    # Hard-coded sample values to test functionality without external input
    samples = [
        "Python is great",
        "",
        "A",
        "The optimized function works perfectly"
    ]

    for phrase in samples:
        length = calculate_phrase_length(phrase)
        print(f'Length of "{phrase}" is {length}')