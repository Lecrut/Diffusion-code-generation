"""
Utility module to build strings from arbitrary sequences of parts with customizable joining mechanisms.
This module provides a flexible function `join_parts` that accepts an iterable of string parts 
and an optional separator argument, returning the joined result as a single string.
It is designed for scenarios requiring dynamic text construction without external dependencies or I/O operations.

Author: AI Assistant
Date: 2023-10-27
"""

def join_parts(parts, separator=''):
    """
    Joins an iterable of strings into a single string with the specified separator.

    Args:
        parts (iterable): An iterable containing elements to be joined as strings. 
                          If any element is not a string, it will be converted to one via str().
        separator (str): The string used to join the parts. Defaults to an empty string ('').

    Returns:
        str: A single string resulting from joining all input parts with the specified separator.

    Raises:
        TypeError: If 'parts' is not iterable or if any element in 'parts' cannot be converted to a string.

    Example usage (see main block).
    """
    # Validate that inputs are provided and convertible
    try:
        result_parts = [str(part) for part in parts]
    except Exception as e:
        raise TypeError(f"Unable to convert all elements of 'parts' to strings. Error details: {e}") from None

    return separator.join(result_parts)

if __name__ == '__main__':
    # Sample test cases demonstrating the flexibility of join_parts
    
    # Test Case 1: Default behavior (no separator)
    sample_list_1 = ["Hello", "World"]
    output_1 = join_parts(sample_list_1)
    
    # Test Case 2: Space as separator
    sample_list_2 = ["Python", "is", "great"]
    output_2 = join_parts(sample_list_2, ' ')
    
    # Test Case 3: Comma and space as separator
    sample_list_3 = [10, 20, 30]
    output_3 = join_parts(sample_list_3, ', ')
    
    # Test Case 4: Custom custom delimiter (pipe)
    sample_list_4 = ["A", "B", "C"]
    output_4 = join_parts(sample_list_4, '|')

    print(f"Test 1 - No separator:\n{output_1}\n")
    print(f"Test 2 - Space separator:\n{output_2}\n")
    print(f"Test 3 - Comma space separator (numeric inputs):\n{output_3}\n")
    print(f"Test 4 - Pipe separator:\n{output_4}")