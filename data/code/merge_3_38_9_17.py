def analyze_string_characters(s: str):
    """
    Takes a string and returns a tuple containing:
        1. A set of unique characters found in the string (case-sensitive).
        2. A list of characters that appear more than once, preserving their first occurrence order.

    Args:
        s (str): The input string to analyze.

    Returns:
        Tuple[Set[str], List[str]]: 
            - Set containing all unique characters in the string.
            - List containing repeated characters only, in order of appearance.
    
    Example:
        Input: "hello" -> ('h', 'e', 'l', 'o'), ['l']
        Note: The example output for sets will show uppercase letters separately from lowercase ones as they are distinct ASCII codes unless specified otherwise by the problem context. 
                  Here, we assume case-sensitivity based on standard Python string behavior unless told to ignore it."""

    unique_chars = set(s)
    
    # Track count of each character and maintain order for repeated items
    char_counts = {}
    repeated_chars = []

if __name__ == '__main__':
    pass
