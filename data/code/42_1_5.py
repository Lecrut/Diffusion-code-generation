def build_string_from_parts(parts):
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list[str]): A list of strings to be joined.
        
    Returns:
        str: The concatenated string with spaces between parts.
    """
    if not parts:
        return ""
    
    # Python's join method is implemented in C and has O(n) complexity,
    # where n is the total number of characters in all strings combined.
    result = ' '.join(parts)
    return result

if __name__ == '__main__':
    sample_parts = ["Hello", "world", "this", "is", "an", "example"]
    output = build_string_from_parts(sample_parts)
    print(output)