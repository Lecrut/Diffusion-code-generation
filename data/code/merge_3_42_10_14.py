def build_string_from_parts(parts: list[str], separator: str | None = None) -> str:
    """
    Concatenates a list of strings with an optional separator.

    Args:
        parts (list[str]): A list of string elements to concatenate.
        separator (str, optional): The string to insert between each element in the list.
                                  If not provided or None, no separator is used.

    Returns:
        str: The concatenated result as a single string.

    Raises:
        TypeError: If 'parts' contains non-string elements.
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")

    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All items in the input list must be strings, got {type(item).__name__}.")

    # Handle empty lists by returning an empty string immediately.
    if len(parts) == 0:
        return ""

    result = parts[0]
    
    # Iterate from the second element to avoid index out of bounds and handle separator logic correctly.
    for i in range(1, len(parts)):
        current_part = parts[i]
        
        # If a separator is provided, join it with the previous part before adding the new one.
        if separator:
            result += separator + current_part
        else:
            result += current_part

    return result

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input or external dependencies.
    
    # Test case 1: Normal list with a separator
    sample_list_1 = ["Hello", " ", "World"]
    sep_1 = "-"
    output_1 = build_string_from_parts(sample_list_1, sep_1)
    print(f"Test 1 (With Separator): '{output_1}'")

    # Test case 2: Empty list
    sample_list_2 = []
    output_2 = build_string_from_parts(sample_list_2)
    print(f"Test 2 (Empty List): '{output_2}'")

    # Test case 3: Single element with separator provided (should ignore extra logic, just return the string)
    sample_list_3 = ["Only"]
    output_3 = build_string_from_parts(sample_list_3, ", ")
    print(f"Test 3 (Single Element): '{output_3}'")

    # Test case 4: Multiple elements without separator
    sample_list_4 = ["Apples", "Bananas", "Cherries"]
    output_4 = build_string_from_parts(sample_list_4)
    print(f"Test 4 (No Separator): '{output_4}'")

    # Test case 5: List with empty strings and separator
    sample_list_5 = ["A", "", "B"]
    sep_5 = "|"
    output_5 = build_string_from_parts(sample_list_5, sep_5)
    print(f"Test 5 (With Empty String): '{output_5}'")

    # Verification of expected outputs for clarity in the console run.
    assert output_1 == "Hello-World", f"Expected 'Hello-World', got '{output_1}'"
    assert output_2 == "", f"Expected empty string, got '{output_2}'"
    assert output_3 == "Only", f"Expected 'Only', got '{output_3}'"
    assert output_4 == "ApplesBananasCherries", f"Expected concatenated without sep, got '{output_4}'"
    assert output_5 == "A||B", f"Expected 'A| |B' (note: empty string adds nothing between A and B if separator is strictly inserted before next), actually logic inserts separator then part. Let's trace: Start='A'. i=1, curr='', sep='|', result += '|' + '' -> 'A|'. i=2, curr='B', result += '|' + 'B' -> 'A||B'. Correct."
    print("All tests passed.")