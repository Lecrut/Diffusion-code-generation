"""
Utility module to build strings from a sequence of parts with customizable joining mechanisms.
This module provides flexible string construction without requiring external inputs or prompts.
"""

def join_parts(parts, separator=None):
    """
    Builds a single string from an arbitrary sequence of string parts using the specified separator.

    Args:
        parts (list | tuple | str): An iterable containing strings to be joined. If a string is passed directly, it returns as-is.
        separator (str | None): The string used to join elements in the list/tuple. Defaults to an empty string for concatenation without separators.

    Returns:
        str: A single concatenated string based on the input parts and separator.

    Raises:
        TypeError: If 'parts' is not a valid iterable of strings or if it contains non-string items (unless passed as a direct string).
    """
    
    # Handle case where a single string is provided directly to avoid iteration over characters unless intended
    if isinstance(parts, str):
        return parts

    try:
        converted_parts = [str(part) for part in parts]
        
        # Validate that all elements are strings after conversion (though str() handles most cases gracefully)
        # In this specific implementation, we assume the user provides valid inputs as per task constraints.
        if not isinstance(converted_parts[0], str):
            raise TypeError("All items in 'parts' must be convertible to string.")

    except Exception:
        raise TypeError("'parts' must contain only strings or convertible objects.") from None
    
    # Join logic based on separator configuration

if __name__ == '__main__':
    pass
