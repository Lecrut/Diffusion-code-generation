def build_string_from_parts(parts):
    """
    Joins a list of string parts with spaces, ensuring O(n) time complexity.
    
    Args:
        parts (list[str]): List of strings to be joined.
        
    Returns:
        str: The joined string separated by spaces.
    """
    # In Python, the built-in join method is implemented in C and runs in linear time relative to total characters n.
    return ' '.join(parts)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "Is", "An"]
    result = build_string_from_parts(sample_parts)
    print(result)