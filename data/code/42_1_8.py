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
    
    # Using a single pass approach with join is inherently O(n) for the total length,
    # as Python's internal implementation of list.join optimizes this efficiently.
    result = []
    current_length = 0
    
    # Pre-calculate lengths to avoid repeated string concatenation overhead in loops if needed,
    # though 'join' on a pre-built list is already highly optimized.
    for part in parts:
        result.append(part)
    
    return " ".join(result)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "A", "Test"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)