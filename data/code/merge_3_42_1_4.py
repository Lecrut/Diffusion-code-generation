def build_string_from_parts(parts: list) -> str:
    """
    Joins a list of string parts with spaces as separators in O(n) time complexity.
    
    Args:
        parts (list): A list containing strings to be joined.
        
    Returns:
        str: The resulting concatenated string separated by single spaces.
    """
    if not parts:
        return ""
    
    result = []
    for part in parts:
        # Ensure each element is a string before appending (handles edge cases)
        processed_part = str(part)
        result.append(processed_part)

    # Join using the separator, which takes O(n+m) where n is number of items and m is total length
    return " ".join(result)

if __name__ == '__main__':
    sample_parts = ["Hello", "World", "This", "is", "an"]
    
    joined_string = build_string_from_parts(sample_parts)
    
    print(joined_string)

    # Additional test case with empty list
    empty_result = build_string_from_parts([])
    assert empty_result == "", f"Expected empty string, got '{empty_result}'"
    
    # Test case with single element
    single_test = ["Only"]
    expected_single = "Only"
    result_single = build_string_from_parts(single_test)
    assert result_single == expected_single, f"Test failed for single item: {result_single} != {expected_single}"

    print("All tests passed.")