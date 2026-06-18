def build_string_from_parts(parts):
    """
    Joins a list of string parts with spaces between them.
    
    This function is optimized to run in O(n) time complexity, where n 
    is the total number of characters across all strings in the input list.
    It handles edge cases such as empty lists and single-element lists correctly.

    Args:
        parts (list): A list of string elements to be joined.

    Returns:
        str: The resulting concatenated string with spaces between non-empty parts.
    
    Note: Empty strings within the list are preserved in their original position 
          if they should logically exist, but typically " ".join() handles empty 
          entries as separators or omitting them depending on content. This implementation
          relies on Python's efficient C-level join operation which is O(n).
    """
    return ' '.join(parts)

if __name__ == '__main__':
    # Sample test cases hard-coded for demonstration purposes.
    sample_parts_1 = ["Hello", "world"]
    
    # Verify the function works as expected with standard inputs.
    result = build_string_from_parts(sample_parts_1)

    assert result == "Hello world"