"""
Flexible string builder utility function.

This module provides a `build_string` function that concatenates an iterable of strings 
into a single result, allowing custom control over the separator used between elements.
It supports various join mechanisms including no separator, space, comma, or any user-defined delimiter.
The implementation is flexible and handles empty sequences gracefully by returning an empty string.

Usage Example:
    >>> parts = ["Hello", "World"]
    >>> build_string(parts, sep=", ")  # Output: Hello, World
    >>> build_string(["a", "b"], "")   # Output: ab
"""

def build_string(sequence_parts: list[str], separator: str) -> str:
    """
    Builds a string from an arbitrary sequence of parts with a specified join mechanism.

    Args:
        sequence_parts (list): A list containing the strings to be concatenated.
                               If empty, returns an empty string regardless of separator.
        separator (str): The string used as a delimiter between elements in `sequence_parts`. 
                        Defaults to an empty string for direct concatenation without separators.

    Returns:
        str: The resulting joined string based on the provided parts and separator.

    Raises:
        TypeError: If `sequence_parts` is not a list or if any element within it is not a string.
    
    Examples:
        >>> build_string(["apple", "banana"], ", ")
        'apple, banana'
        
        >>> build_string([10, 20], sep="") 
        TypeError: Elements must be strings.

    Note:
        This function assumes the input `sequence_parts` is a list of valid string objects.
        Non-string elements will raise a Type Error to ensure data integrity in subsequent processing.
    """
    
    # Validate that sequence_parts is actually a list and contains only strings
    if not isinstance(sequence_parts, list):
        raise TypeError(f"Expected 'sequence_parts' to be a list, got {type(sequence_parts).__name__}")

    for item in sequence_parts:
        if not isinstance(item, str):
            raise TypeError("All elements within 'sequence_parts' must be strings.")

    # Use the built-in join method which is efficient and handles edge cases like empty lists correctly.
    return separator.join(sequence_parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    # Sample 1: Joining with a comma and space (default-like behavior but explicit)
    parts_1 = ["Python", "is", "awesome"]
    result_1 = build_string(parts_1, sep=", ")

    # Sample 2: No separator between elements
    parts_2 = ["a", "b", "c"]
    result_2 = build_string(parts_2, sep="")

    # Sample 3: Joining with a custom delimiter (pipe symbol)
    parts_3 = ["root", "user", "process"]
    result_3 = build_string(parts_3, sep="|")

    # Printing results to verify execution without any prompts or files access
    print(f"Sample 1 - Comma separated: {result_1}")
    print(f"Sample 2 - No separator: '{result_2}'")
    print(f"Sample 3 - Pipe delimited: {result_3}")

    # Additional test case with an empty list to ensure robustness
    parts_empty = []
    result_empty = build_string(parts_empty, sep="|")
    assert result_empty == "", "Empty list should produce empty string."
    
    print("All tests passed successfully.")