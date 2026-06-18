"""Utility module containing a static method to calculate string length."""

def _normalize_string(input_str: str) -> str:
    """Normalize input by stripping whitespace if needed, though not strictly required here.
    
    This helper ensures consistent handling of edge cases like None or empty strings.
    """
    return input_str.strip() if isinstance(input_str, str) else ""

def calculate_length(text: object) -> int:
    """Calculate the length of a string after normalization.

    Args:
        text (object): The input to measure. If not a string, it is treated as empty.

    Returns:
        int: The normalized length of the input string.
    
    Raises:
        TypeError: Only if an unexpected non-string type is passed that isn't handled by defaults.
                   However, per Python conventions and task constraints, we handle gracefully 
                   to avoid unnecessary exceptions for simple types unless explicitly needed.
                   Here, we assume any non-string should result in 0 length effectively.

    Example:
        >>> calculate_length("Hello World")
        11
        >>> calculate_length("")
        0
        >>> calculate_length(None)
        0
    """
    normalized = _normalize_string(text) if isinstance(text, str) else ""
    
    # Ensure we are dealing with a string before measuring length to avoid TypeError on non-string types like lists or ints
    try:
        return len(normalized)
    except Exception as e:  # Fallback for any unexpected type errors during normalization
        print(f"Warning: Unexpected error while calculating length. Type of input was not standard string.")
        raise

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user interaction
    
    samples = [
        "Hello, Python!",
        "",
        None,
        12345,
        ["list", "of", "strings"],
        "   Multiple   Spaces   ",
    ]

    print("Sample Length Calculations:")
    for sample in samples:
        try:
            length = calculate_length(sample)
            # Determine display name based on type to keep output clean
            if isinstance(sample, str):
                label = f"'{sample}'"
            elif isinstance(sample, list):
                label = repr(sample)
            else:
                label = str(type(sample).__name__) + ":" + str(sample)
            
            print(f"{label}: {length}")
        except Exception as ex:
            print(f"{repr(ex)}")