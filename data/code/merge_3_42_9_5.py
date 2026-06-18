"""
Utility module to build strings from arbitrary sequences with customizable joining mechanisms.
This module provides a flexible function to concatenate string parts using various separators 
or without any separator, suitable for general utility purposes.
"""

def join_parts(parts: list, sep=None) -> str:
    """
    Builds a single string from an arbitrary sequence of string parts.

    Args:
        parts (list): A list containing zero or more strings to be joined.
        sep (str, optional): The separator string used between elements in the list. 
                            If None, no separation is applied directly; instead, individual items are concatenated.
                            
    Returns:
        str: A single string resulting from joining all parts with the specified separator if applicable.

    Examples:
        >>> join_parts(["Hello", "World"], ", ")
        'Hello, World'
        >>> join_parts([1, 2], sep="") # Note: This handles non-string input by converting to str implicitly for demonstration logic in this specific scope if needed, but strictly typing suggests strings. To ensure robustness with mixed types as per typical use cases without external deps, we assume inputs are strings or convert them internally if necessary based on common utility patterns. However, strict adherence implies string parts. Let's stick to string input spec for safety unless specified otherwise in general Pythonic way which often converts.
        >>> # Correct usage assuming strings: join_parts(["a", "b"], "-") -> 'a-b'

    Note: 
    The function assumes `parts` contains strings. If non-string items are encountered, they will be converted to str automatically for seamless utility in most scenarios unless strict typing is enforced externally.
    
    >>> join_parts([10, 20], sep=" ") # Implicit conversion example if needed? No, let's stick to pure string logic as per "string parts" requirement description but make it robust by converting each part to str first.
    """

    # Ensure all items are treated as strings for maximum flexibility in joining
    processed_parts = [str(part) for part in parts]
    
    if sep is None:
        return "".join(processed_parts)
    else:
        return sep.join(processed_parts)

if __name__ == '__main__':
    # Sample test cases to demonstrate functionality without any user input, network access, or external files.

    sample_cases = [
        (["Hello", "World"], ", "),  # Standard comma separated with space
        ([10, 20], ""),              # Integers joined as strings with no separator
        (["a", "b", "c"], "-"),      # Hyphenated list
        ([], ","),                    # Empty list handling
        ("Single Item", None),       # Single item in a string vs list? The signature expects list. Adjusting sample to match type hint:
    ]

    # Corrected samples ensuring 'parts' is always a list per function definition
    
    test_inputs = [
        (["Hello", "World"], ", "), 
        ([10, 20], ""),              # Converts ints to str internally via join_parts logic inside or just passes as string parts? Let's assume user provides strings mostly but conversion happens. Re-reading task: 'arbitrary sequence of string parts'. So input should be strings.
    ]

    print("Testing flexible utility function:\n")

    for i, (parts_data, separator) in enumerate(test_inputs):
        # Ensure types are consistent with the docstring logic which converts to str anyway
        result = join_parts(parts_data if isinstance(parts_data, list) else [parts_data], sep=separator)
        
        print(f"Test Case {i+1}:")
        print(f"  Input parts: {parts_data}")
        print(f"  Separator: '{separator}' (None means no separator)")
        print(f"  Output Result: '{result}'\n")

    # Additional specific demonstration for empty and single element cases not fully covered in initial list above if needed, 
    # but the main block runs successfully with provided samples.
    
    extra_demo = [join_parts(["Apples", "Bananas"], ", "), join_parts([], "-")]
    print("Additional quick checks:")
    for item in extra_demo:
        print(f"  {item}")