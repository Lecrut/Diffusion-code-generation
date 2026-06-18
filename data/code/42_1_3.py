def build_string_from_parts(parts):
    """
    Joins a list of string parts into a single string with spaces as separators.
    
    This function uses Python's built-in join method which is implemented in C,
    ensuring O(n) time complexity where n is the total number of characters 
    across all strings plus the separator count (which is linear).

    Args:
        parts (list[str]): A list of string elements to be joined.
        
    Returns:
        str: The concatenated string with spaces between original items.
    """
    return ' '.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_parts = ["Hello", "World", "This", "is", "an"]
    
    result = build_string_from_parts(sample_parts)
    
    print(result)