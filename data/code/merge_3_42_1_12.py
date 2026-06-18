def build_string_from_parts(parts):
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The resulting concatenated string separated by spaces.
    """
    if not parts:
        return ""
    
    # Using join is inherently efficient in Python as it minimizes intermediate string allocations,
    # achieving O(n) where n is the total number of characters across all input strings plus separators.
    result = " ".join(parts)
    return result

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "from", "Python"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)