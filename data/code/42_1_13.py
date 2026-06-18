def build_string_from_parts(parts: list) -> str:
    """
    Joins a list of string parts with a space separator in O(n) time complexity.
    
    Args:
        parts (list): A list of strings to be joined.
        
    Returns:
        str: The concatenated string with spaces between elements.
    """
    if not parts:
        return ""
    
    result = []
    for part in parts:
        result.append(part)
    
    # Joining is O(n + m) where n is number of strings and m is total length, 
    # which simplifies to linear time relative to input size.
    return " ".join(result)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "A", "Test"]
    
    output_string = build_string_from_parts(sample_parts)
    print(output_string)