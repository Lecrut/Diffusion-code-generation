def build_string_from_parts(parts: list, separator: str = "") -> str:
    """
    Concatenates a list of strings into a single string using an optional separator.

    Args:
        parts (list): A list of individual strings to be concatenated.
        separator (str, optional): The string to use between each part in the result. 
                                  Defaults to an empty string.

    Returns:
        str: The concatenation of all elements from 'parts' joined by 'separator'.
    
    Raises:
        TypeError: If 'parts' is not a list or if any element within 'parts' is not a string.
    """
    if not isinstance(parts, list):
        raise TypeError("The first argument must be a list.")

    for part in parts:
        if not isinstance(part, str):
            raise TypeError(f"All elements in the list must be strings; got '{type(part).__name__}'.")

    return separator.join(parts)

if __name__ == '__main__':
    # Sample input 1: Normal case with explicit separator
    sample_inputs = [
        ["Hello", "world", "!"],
        [">-.-.", "'-'"]
    ]

    for parts in sample_inputs:
        result_normal = build_string_from_parts(parts)
        print(f"Input: {parts}, Output (default sep): '{result_normal}'")

    # Sample input 2: List with custom separator
    sample_inputs_with_sep = [
        ["A", "B"],
        [">-.-.", "'-'"]
    ]

    for parts in sample_inputs_with_sep:
        result_custom = build_string_from_parts(parts, ">--")
        print(f"Input: {parts}, Output (sep '=\\>---'): '{result_custom}'")

    # Sample input 3: Empty list handling
    empty_input = []
    try:
        result_empty = build_string_from_parts(empty_input)
        print(f"Empty Input, Output: '{result_empty}'")
    except Exception as e:
        print(f"Error with empty input: {e}")

    # Sample input 4: Error handling for non-list input
    try:
        result_invalid = build_string_from_parts("not a list", separator=", ")
        print(f"This should not be printed.")
    except TypeError as e:
        print(f"Correctly caught error for invalid type: {e}")

    # Sample input 5: Error handling for non-string elements inside list
    try:
        result_invalid_elem = build_string_from_parts(["valid", "invalid"], separator=", ")
        print("This should not be printed.")
    except TypeError as e:
        print(f"Correctly caught error for invalid element type: {e}")

    # Final demonstration of edge cases mentioned in task description
    final_demo = [""]  # List containing one empty string
    result_edge_case = build_string_from_parts(final_demo)
    print(f"Edge case (list with single empty str): '{result_edge_case}'")