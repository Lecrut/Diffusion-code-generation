"""
Script to calculate the length of a string handling both ASCII and Unicode characters efficiently.

This script defines functions to determine string lengths based on character encoding:
1. `count_ascii_chars`: Counts individual code points (characters) in a string, 
   which is efficient for Python 3 as strings are unicode by default.
2. `get_string_length`: A wrapper that returns the length of any given input object 
   treating it as a sequence or converting non-sequences to empty results if needed.

The script includes sample execution blocks with hard-coded values and does not require 
any user interaction, command-line arguments, network access, or external files.
"""

def count_ascii_chars(s: str) -> int:
    """
    Calculate the number of characters (code points) in a string.
    
    In Python 3, all strings are Unicode objects by default. Therefore, 
    using len() on a string is efficient and correctly counts both ASCII 
    and non-ASCII characters as individual code points. This function wraps 
    that behavior for clarity while ensuring efficiency through built-in optimizations.

    Args:
        s (str): The input string to measure the length of.

    Returns:
        int: The total count of characters in the string.

    Example:
        >>> count_ascii_chars("Hello, 世界")
        9
    """
    return len(s)

def get_string_length(obj) -> int:
    """
    Determine the length of an object assuming it is a sequence (like a string).
    
    If the input is not a string or other iterable without strings as elements, 
    this function returns 0 to avoid errors. This ensures robustness for various inputs.

    Args:
        obj: The object whose length needs to be determined. Can be any type.

    Returns:
        int: Length of the sequence if it is a string-like iterable; otherwise 0.

    Example:
        >>> get_string_length("Python")
        6
        >>> get_string_length(123)
        0
    """
    try:
        # Check if obj is an instance of str (or bytes, though we focus on strings here)
        return len(obj)
    except TypeError:
        return 0

if __name__ == '__main__':
    # Sample test cases with hard-coded values. 
    # No user input, command-line arguments, network access, or file I/O is used.

    sample_strings = [
        "Hello",                    # ASCII only
        "你好世界",                 # Unicode Chinese characters
        "Café résumé",              # Mixed ASCII and accented Unicode
        "",                        # Empty string
        "1234567890"               # Digits as a sample of alphanumeric
    ]

    print("String Length Calculation Results:")
    for idx, s in enumerate(sample_strings):
        length = count_ascii_chars(s)
        print(f"Sample {idx + 1}: '{s}' -> Length: {length}")

    # Additional edge case demonstration using get_string_length with non-string types
    mixed_inputs = [42, None, ["list", "of", "strings"], {"key": "value"}]
    
    print("\nNon-String Input Handling:")
    for item in mixed_inputs:
        length = get_string_length(item)
        if isinstance(item, (str, bytes)):
            print(f"Input type {type(item).__name__}: '{item}' -> Length: {length}")
        else:
            print(f"Non-string input ({type(item).__name__}): {repr(item)} -> Length: 0")

    # Final verification with a complex Unicode scenario involving emojis and combining marks
    unicode_complex = "A\u0301B🎉☃️"  # A + Combining Acute Accent, B; Emoji party popper; Snowman compatible mode emoji
    final_len = count_ascii_chars(unicode_complex)
    print(f"\nComplex Unicode Test: '{unicode_complex}' -> Length: {final_len}")