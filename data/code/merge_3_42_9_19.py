"""
Utility module to build strings from arbitrary sequences of parts with customizable joining mechanisms.
This module provides a flexible function `build_string` that accepts an iterable of string parts 
and a separator, defaulting to empty string if not specified. It also includes helper functions 
for common joining patterns like space-separated or comma-separated lists.

No external libraries are required. The code is self-contained and runs without user input
or network access when executed directly via the provided main block.
"""

def build_string(parts, separator=""):
    """
    Builds a string from an arbitrary sequence of parts using a specified separator.

    Args:
        parts (iterable): An iterable containing elements to be joined into a single string.
                          Elements will be converted to strings automatically.
        separator (str): The string used to separate the individual part strings in the output.
                        Defaults to an empty string ("").

    Returns:
        str: A single string resulting from joining all parts with the specified separator.

    Examples:
        >>> build_string(["a", "b"], ",")
        'a,b'
        >>> build_string([1, 2], "-")
        '1-2'
        >>> build_string([], ": ")
        ''
    """
    if not isinstance(parts, (list, tuple)):
        try:
            parts = list(parts)
        except TypeError:
            # If it's a single non-string object that isn't iterable in the expected way, wrap it.
            return str(parts)

    return separator.join(str(part) for part in parts)

def join_space(*parts):
    """Convenience function to join parts with spaces."""
    return build_string(list(parts), " ")

def join_comma(*parts):
    """Convenience function to join parts with commas and a space."""
    return build_string(list(parts), ", ")

if __name__ == '__main__':
    # Sample test cases demonstrating the functionality without any user input.

    sample_data_1 = ["Hello", "World"]
    result_space = join_space(sample_data_1[0], sample_data_1[1])
    
    print("Space separated:", repr(result_space))  # Expected: 'Hello World'

    sample_data_2 = [42, True]
    result_default = build_string(sample_data_2)
    
    print("Default (empty separator):", repr(result_default))  # Expected: '42True' or similar depending on conversion
    
    sample_data_3 = ["apple", "banana", "cherry"]
    result_comma = join_comma(*sample_data_3)
    
    print("Comma separated:", repr(result_comma))  # Expected: 'apple, banana, cherry'

    empty_list_result = build_string([])
    print("Empty list result:", repr(empty_list_result))  # Expected: ''