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
    
    # Using a generator expression with join ensures O(n) complexity as it iterates once,
    # avoiding the quadratic time complexity of repeated concatenation in loops.
    result = " ".join(parts)
    return result

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "An"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)