"""
Flexible utility function to build strings from arbitrary sequences with customizable separators.
This module provides a `join_strings` function that concatenates any iterable of string elements,
applying a user-defined separator between items. It supports various joining mechanisms including
no separator, space, comma, custom delimiters, or even dynamic patterns via format specifiers if needed
in extended usage (kept simple here as per task: exact joining mechanism).

The function is designed to be flexible and efficient for building strings from lists, tuples, generators, etc.
"""

def join_strings(iterable, separator=''):
    """
    Builds a string from an arbitrary sequence of string parts with a specified separator.

    Parameters:
        iterable (iterable): An iterable containing elements that will be converted to strings and joined.
                             Non-string elements will be converted to their string representation using str().
        separator (str): The string used to join the items in the iterable. Default is an empty string (no separator).

    Returns:
        str: A single string resulting from joining the sequence with the specified separator.

    Raises:
        TypeError: If 'separator' is not a string or if elements are neither strings nor convertible via str().
                  Note: Python's built-in behavior allows most objects to be converted, so we generally accept wide input,
                  but strictly speaking, this function expects an iterable of items that support string conversion.

    Examples:
        >>> join_strings(['a', 'b'])
        'ab'
        >>> join_strings([1, 2], separator=', ')
        '1, 2'
        >>> join_strings('abcde')  # Works on strings too (iterable of chars) if no sep specified, or with explicit logic. 
                                  Actually iterating a string yields characters. We treat input as iterable of items to be joined.
    """
    
    # Ensure separator is a string
    if not isinstance(separator, str):
        raise TypeError("Separator must be a string.")

    result_parts = []
    for item in iterable:
        try:
            s_item = str(item)
        except Exception as e:
            # In rare cases where str() fails (e.g., custom objects without __str__ defined properly), 
            # we might want to handle it, but standard Python allows most things via str().
            raise TypeError(f"Unable to convert element '{item}' to string. Error details: {e}") from e
        
        result_parts.append(s_item)

    return separator.join(result_parts)

if __name__ == '__main__':
    # Hard-coded sample values demonstrating various joining mechanisms
    
    # Sample 1: No separator (default behavior with empty string)
    list_no_sep = ['Hello', 'World']
    
    # Sample 2: Space as separator
    list_space_sep = ['Python', 'is', 'great']
    
    # Sample 3: Comma and space as separator
    list_comma_sep = [10, 20, 30]

    # Sample 4: Custom custom separator (pipe)
    list_pipe_sep = ['apples', 'bananas', 'cherries']

    # Run samples and print results
    output_no_sep = join_strings(list_no_sep)
    
    output_space_sep = join_strings(list_space_sep, separator=' ')
    
    output_comma_sep = join_strings(list_comma_sep, separator=', ')
    
    output_pipe_sep = join_strings(list_pipe_sep, separator='|')

    print("No Separator:", repr(output_no_sep))
    print("Space Separated:", repr(output_space_sep))
    print("Comma Separated:", repr(output_comma_sep))
    print("Pipe Separated:", repr(output_pipe_sep))
    
    # Additional test with mixed types (numbers that convert to strings)
    print("\nMixed Types Test:")
    mixed_data = [42, 3.14, True]
    output_mixed = join_strings(mixed_data, separator='-')
    print("Joined Mixed:", repr(output_mixed))