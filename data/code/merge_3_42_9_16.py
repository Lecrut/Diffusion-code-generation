"""
Flexible String Builder Utility Module.

This module provides a utility function to construct strings from an arbitrary sequence of parts,
with customizable joining mechanisms such as no separator, space, or comma.
"""

def build_string(parts: list[str], joiner: str = "") -> str:
    """
    Builds a single string from a list of input parts using the specified joiner.

    Args:
        parts (list): A list of strings to be joined together.
        joiner (str, optional): The separator string used between elements in 'parts'. Defaults to an empty string.

    Returns:
        str: The resulting concatenated string.

    Examples:
        >>> build_string(["Hello", "World"], ",")
        'Hello, World'
        >>> build_string(["a", "b", "c"])
        'abc'
    """
    return joiner.join(parts)

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without user input.

    sample_data_1 = ["Python", "is", "awesome"]
    result_space = build_string(sample_data_1, " ")
    print(f"Joined with space: '{result_space}'")  # Expected output: 'Python is awesome'

    sample_data_2 = [".", ".", "."]
    result_comma = build_string(sample_data_2, ",")
    print(f"Joined with comma: '{result_comma}'")  # Expected output: '. . .'

    sample_data_3 = ["Start"]
    result_none_joiner = build_string(sample_data_3)
    print(f"No joiner (single item): '{result_none_joiner}'")  # Expected output: 'Start'

    empty_input = []
    result_empty = build_string(empty_input, ", ")
    print(f"Empty input list: '{result_empty}'")  # Expected output: ''