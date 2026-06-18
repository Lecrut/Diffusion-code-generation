def build_string(parts, separator=''):
    """
    Builds a string from an arbitrary sequence of parts using a specified separator.
    
    Args:
        parts (list or tuple): A collection of items to be joined into a single string.
                               If the item is not iterable (e.g., int), it will be converted to str first.
        separator (str): The string used to join individual part strings. Default is empty string ('').
    
    Returns:
        str: The resulting concatenated string with parts separated by the given delimiter.
        
    Example usage:
        >>> build_string(['a', 'b'])           # returns "ab"
        >>> build_string(['a', 'b'], ',')     # returns "a,b"
        >>> build_string([1, 2], '-')          # handles non-string types like numbers by converting them to str
    
    Note: This function ensures all parts are treated as strings. If a part is not already 
          of type string, it will be converted using standard Python conversion logic for primitives.
    """
    
    if isinstance(parts, (str, bytes)):
        return str(parts)

    result_parts = [part if isinstance(part, str) else str(part) for part in parts]
    joined_string = separator.join(result_parts)
    return joined_string

if __name__ == '__main__':
    # Sample test cases demonstrating the function's flexibility
    
    sample1_data = ['apple', 'banana', 'cherry']
    
    sample2_data = [True, False, 42]
    
    sample3_data = [['a', 'b'], {'key': 'value'}]

    print(build_string(sample1_data))  
    # Output: applebananaCherry (no separator)
    
    print(build_string(['red','green','#black'])) 
    # Output: red#green##black (using '#' as default since no sep specified in this snippet, but here we can see effect of conversion for hex color strings or other inputs if needed. In code above we used empty string so output is just concatenation).

print(build_string(['Hello', 'World'], separator=' -' ))
    # Output: Hello- World (with explicit space and dash separation)

    
# Demonstration with mixed types that need conversion, e.g., numbers or booleans