"""
Utility module to build strings from arbitrary sequences with customizable joining mechanisms.
This module provides a flexible function that can join string parts without separators, 
with spaces, commas, or any custom separator provided by the user.
"""

def build_string(parts: list[str], sep: str = "") -> str:
    """
    Builds a single string from an arbitrary sequence of string parts with a specified separator.

    Args:
        parts (list[str]): A list of strings to be joined together.
        sep (str): The separator string used between each part in the list. Defaults to empty string.

    Returns:
        str: The resulting concatenated string based on the provided separator.

    Examples:
        >>> build_string(["Hello", "World"], ", ")
        'Hello, World'
        >>> build_string([1, 2, 3], sep="") -> TypeError (int not allowed per type hint logic in real usage, but handled gracefully below if needed? 
        Note: The prompt specifies string parts. We enforce list of strings.)
    """
    # Validate that all elements are actually strings to ensure robustness
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements must be strings, but got {type(item).__name__}: '{item}'")

    return sep.join(parts)

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    sample_list_1 = ["Python", "is", "amazing"]
    result_no_sep = build_string(sample_list_1, "")
    
    sample_list_2 = ["Apple", "Banana", "Cherry"]
    result_space_sep = build_string(sample_list_2, " ")
    
    sample_list_3 = ["Item 1", "Item 2", "Item 3"]
    result_comma_sep = build_string(sample_list_3, ",")

    print(f"Joined with no separator: '{result_no_sep}'")
    print(f"Joined with space separator: '{result_space_sep}'")
    print(f"Joined with comma separator: '{result_comma_sep}'")