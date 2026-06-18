"""
Module to calculate the length of a string handling both ASCII and Unicode characters efficiently.

This module provides two functions:
1. `length_ascii` - Calculates length assuming all characters are single-byte (ASCII).
2. `length_unicode` - Calculates actual character count, respecting multi-byte Unicode sequences.

The script includes a main execution block with hard-coded sample values to demonstrate functionality
without requiring user input or external dependencies.
"""

def _is_ascii(s: str) -> bool:
    """Check if the string contains only ASCII characters."""
    try:
        s.encode('ascii')
        return True
    except UnicodeEncodeError:
        return False

def length_ascii(s: str) -> int:
    """
    Calculate the byte length of a string assuming it is pure ASCII.

    Args:
        s (str): The input string to measure.

    Returns:
        int: The number of bytes if all characters are ASCII, otherwise 0 or -1 depending on validity check.
             For this implementation, returns actual byte count only for valid ASCII strings.
    """
    try:
        encoded = s.encode('ascii')
        return len(encoded)
    except UnicodeEncodeError:
        # If not pure ASCII, we cannot give a meaningful "ASCII length" as defined in the task context of handling both types efficiently.
        # We treat invalid input for this specific function by returning -1 to indicate mismatch with assumption.
        return -1

def length_unicode(s: str) -> int:
    """
    Calculate the actual number of characters (Unicode code points) in a string.

    This is the standard definition of 'length' in Python, which counts each character regardless
    of how many bytes it occupies internally or externally. It handles emojis, combining diacritical marks, etc., correctly.

    Args:
        s (str): The input string to measure.

    Returns:
        int: The number of characters in the string.
             If the argument is not a valid string type, returns -1 as an error indicator for this module's context.
    """
    if isinstance(s, str):
        return len(s)
    else:
        # Fallback to handle potential non-string inputs gracefully by returning -1
        return -1

def calculate_string_length(s: str = None) -> int:
    """
    Main utility function to determine string length.

    This is the primary entry point for users who want a single result without choosing between ASCII/Unicode modes explicitly,
    defaulting to Unicode character count as it represents true 'length' in most contexts involving mixed scripts (ASCII + Unicode).

    Args:
        s (str): The input string. Defaults to None which will trigger an error handling path for demonstration purposes or allow passing a specific sample later.

    Returns:
        int: Length of the string as per Unicode standards, or -1 if invalid type passed directly here without explicit mode selection logic in this simplified view. 
             Note: In practice, we usually prefer `length_unicode` unless ASCII constraint is strictly needed.
             For robustness, this function defaults to returning length based on actual characters (Unicode).
    """
    # Default behavior for general use cases is Unicode character count
    return len(s) if isinstance(s, str) else -1

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access used.

    samples = [
        "Hello World",          # Pure ASCII string
        "Café résumé",           # Contains accented characters (Unicode)
        "😀🎉🚀",                 # Emoji string (Multi-byte Unicode)
        "",                     # Empty string edge case
        123,                    # Non-string input for error handling demonstration logic if passed directly to main functions below.
    ]

    print("String Length Calculation Results")
    print("-" * 40)

    for sample in samples:
        try:
            ascii_len = length_ascii(sample)
            unicode_len = len(str(sample)) # Convert non-string inputs to string before counting chars if necessary, though type check handles it
            
            # Special handling for the integer example passed directly as a list element above (123)
            # The function definitions expect str. We will demonstrate on valid strings only 
            # or handle conversion implicitly in this demo block logic below:

            actual_str = sample if isinstance(sample, str) else f"Value({sample})"
            
            ascii_result = length_ascii(actual_str)
            unicode_result = len(str(actual_str))

            print(f"Input: {repr(actual_str)}")
            print(f"  ASCII Length (bytes):     {ascii_result}")
            print(f"  Unicode Length (chars):   {unicode_result}")
            
        except Exception as e:
            # Graceful error handling for unexpected issues in the demo block
            print(f"Input: {sample} -> Error occurred: {e}")

    print("-" * 40)
    
    # Explicit demonstration of default behavior using calculate_string_length
    test_input = "Python is great! 🐍"
    result_default = calculate_string_length(test_input)
    print(f"\nDefault Calculation for '{test_input}': {result_default}")