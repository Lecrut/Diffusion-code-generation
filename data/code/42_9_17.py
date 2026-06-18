"""
Flexible string builder utility function.

This module provides a `build_string` function that constructs a single string 
from an arbitrary sequence of input parts, allowing the user to specify custom joining mechanisms.

Usage:
    result = build_string(parts=['a', 'b'], separator=', ')
    
The function supports various separators including empty strings (no join), spaces, commas, or any other delimiter provided by the user.
"""

def build_string(*parts, separator=''):
    """
    Builds a string from an arbitrary sequence of parts using a specified separator.

    Args:
        *parts: Variable length argument list containing individual string elements to be joined.
        separator (str): The string used to join the parts. Defaults to empty string ('').

    Returns:
        str: A single concatenated string with separators inserted between parts if provided.
    
    Examples:
        >>> build_string('hello', 'world')
        'helloworld'
        
        >>> build_string('apple', 'banana', separator=', ')
        'apple, banana'
        
        >>> build_string(['a', 1, True], separator='|')
        'a|1|True' (Note: non-string parts are converted to strings)
    """
    
    # Convert all input parts to strings if they aren't already
    string_parts = [str(part) for part in parts]
    
    return separator.join(string_parts)

if __name__ == '__main__':
    # Sample test cases demonstrating the functionality without any user interaction
    
    # Test case 1: Default behavior (no separator)
    result_1 = build_string('Hello', 'World')
    print(f"Test 1 - No Separator: '{result_1}'")

    # Test case 2: Space as separator
    result_2 = build_string('Python', 'is', 'great', separator=' ')
    print(f"Test 2 - Space Separator: '{result_2}'")

    # Test case 3: Comma and space as separator with mixed types (converted to string)
    data_points = ['Item A', 10, True]
    result_3 = build_string(*data_points, separator=', ')
    print(f"Test 3 - Mixed Types & Comma Separator: '{result_3}'")

    # Test case 4: Custom custom delimiter (pipe)
    words = ['one', 'two', 'three']
    result_4 = build_string(*words, separator='|')
    print(f"Test 4 - Pipe Separator: '{result_4}'")

    # Verification of expected outputs for clarity in standalone execution
    assert result_1 == "HelloWorld", f"Expected 'HelloWorld', got {result_1}"
    assert result_2 == "Python is great", f"Expected 'Python is great', got {result_2}"
    assert result_3 == "Item A, 10, True", f"Expected 'Item A, 10, True', got {result_3}"
    assert result_4 == "one|two|three", f"Expected 'one|two|three', got {result_4}"

    print("All tests passed successfully.")