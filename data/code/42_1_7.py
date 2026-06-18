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
    
    result = []
    for part in parts:
        # Using append is efficient here as it avoids repeated reallocation 
        # compared to concatenating strings directly with + inside a loop,
        # though Python's string handling is already optimized. We use list join
        # at the end which is implemented in C and runs in O(n).
        result.append(part)
    
    return " ".join(result)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "Python"]
    output_string = build_string_from_parts(sample_parts)
    print(output_string)

    # Additional test case with empty list and single element
    assert build_string_from_parts([]) == ""
    assert build_string_from_parts(["Only"]) == "Only"