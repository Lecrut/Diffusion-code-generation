def build_string_from_parts(parts):
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The concatenated string separated by spaces.
    """
    if not parts:
        return ""
    
    # Using join is inherently optimized in CPython and runs in O(n) time,
    # where n is the total number of characters across all strings plus separators.
    return " ".join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "an", "optimized", "function"]
    result = build_string_from_parts(sample_parts)
    print(result)