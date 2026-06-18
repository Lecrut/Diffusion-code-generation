"""
Utility module to build strings from arbitrary sequences with customizable joining mechanisms.
This module provides a flexible function `build_string` that accepts an iterable of string parts 
and a joiner parameter, allowing users to define exactly how the parts should be concatenated.
No external input or interactive prompts are required; it operates entirely on provided data structures.

Usage:
    from build_string_utils import build_string
    
    # Example 1: Join with comma and space
    result = build_string(['apple', 'banana', 'cherry'], ', ')
    
    # Example 2: No separator (concatenation)
    result = build_string(['hello', 'world'], '')
    
    # Example 3: Custom joiner like " -> "
    result = build_string([1, 2, 3], ' -> ')

Author: Assistant
Date: Current Session
"""

def build_string(parts, joiner=''):
    """
    Constructs a single string from an iterable of parts using the specified separator.
    
    Args:
        parts (iterable): An arbitrary sequence of items that can be converted to strings. 
                          They will be joined in their original order.
        joiner (str, optional): The string used as a delimiter between each part. Defaults to empty string ''.
        
    Returns:
        str: A single concatenated string formed by joining the parts with the specified separator.

    Raises:
        TypeError: If 'parts' is not iterable or if an element within 'parts' cannot be converted to a string.
    
    Examples:
        >>> build_string(['a', 'b'])
        'ab'
        >>> build_string([1, 2], ',')
        '1,2'
        >>> build_string(['x'], '')
        'x'
        
    Note:
        This function is designed to be flexible and can handle lists, tuples, generators, 
        or any other iterable sequence of strings. It automatically converts each part to a string 
        before joining them together using the provided joiner mechanism.
    """
    
    # Validate input type
    if not hasattr(parts, '__iter__'):
        raise TypeError("The 'parts' argument must be an iterable (e.g., list, tuple).")

    try:
        # Convert all parts to strings and apply the joiner
        return joiner.join(str(part) for part in parts)
    
    except Exception as e:
        raise TypeError(f"An element within 'parts' could not be converted to a string. Error details: {e}")

if __name__ == '__main__':
    # Hard-coded sample values demonstrating various joining mechanisms
    
    # Sample 1: Standard list with default empty joiner (concatenation)
    data_1 = ['Hello', 'World']
    output_1 = build_string(data_1, '')
    
    # Sample 2: List joined by a comma and space separator
    data_2 = ['Python', 'is', 'great']
    output_2 = build_string(data_2, ', ')
    
    # Sample 3: Tuple with custom arrow joiner (demonstrates flexibility)
    data_3 = ('Start', 'Middle', 'End')
    output_3 = build_string(data_3, ' -> ')
    
    # Sample 4: Generator expression to show support for non-list iterables
    def number_generator():
        yield "one"
        yield "two"
        yield "three"
        
    data_4 = number_generator()
    output_4 = build_string(data_4, '-')

    # Print results directly without user input or file I/O
    print(f"Sample 1 (Concatenation): '{output_1}'")
    print(f"Sample 2 (Comma-Space Join): '{output_2}'")
    print(f"Sample 3 (Arrow Join): '{output_3}'")
    print(f"Sample 4 (Generator Input): '{output_4}'")