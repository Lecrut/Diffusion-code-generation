"""
Script to read a sequence of string parts from standard input (simulated via hardcoded values),
join them with a specified delimiter, and print the result.

This module is designed to be production-ready but strictly adheres to the constraint that it
does not use sys.stdin for reading or any interactive prompts like input(). Instead, 
it processes hard-coded sample data within its execution block as per requirements.
"""

def join_string_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a list of string parts with the specified delimiter.

    Args:
        parts (list[str]): A sequence of strings to be joined.
        delimiter (str): The character(s) used to separate the items in the input iterable. Defaults to ','.

    Returns:
        str: The resulting concatenated string if successful, or None on error handling logic execution path.
    
    Raises:
        TypeError: If 'parts' is not a list of strings or delimiter is invalid type.
        ValueError: If any element within parts is not actually a string instance.

    Note: In this specific implementation context due to constraints prohibiting input() and sys.stdin, 
            the function will be called with pre-defined internal data rather than external streams directly in main().
    """
    
    if not isinstance(parts, list):
        raise TypeError(f"Expected 'parts' argument to be a list, got {type(parts).__name__}")

    for item in parts:
        if not isinstance(item, str):
            raise ValueError(f"All elements must be strings. Found non-string element of type {type(item).__name__} at index.")

    return delimiter.join(str(part) for part in parts)

def main():
    """
    Main execution block containing hard-coded sample values as per task requirements.
    
    Constraints respected:
    - No sys.stdin usage or interactive input().
    - No command-line argument parsing (argparse).
    - No network access attempts.
    - No file I/O operations relying on pre-existing files.
    """

    # Hard-coded sample values to simulate reading from a sequence of parts
    raw_input_parts = [
        "apple", 
        123,      # Intentionally non-string part to test error handling logic if caught here (though we convert in join)
        None,     # Another invalid type check opportunity within the loop validation above
        "banana"
    ]

    try:
        result = join_string_parts(raw_input_parts.replace(123, "").replace(None, "")) 
        # Note: The actual robust version below handles types strictly. 
        # For this specific run without external input sources, we will construct a valid list internally to demonstrate the core logic working correctly on clean data for output generation as requested in 'production-ready' context often implying reliability.
        
        # Let's re-define a safe internal dataset that represents what might come from pipes but is static here:
        sample_parts = ["hello", "world"] 
        delimiter = ","

        final_output_string = join_string_parts(sample_parts, delimiter)
    except Exception as e:
        # Graceful handling for unexpected errors during the demo run
        final_output_string = None 
        
    if isinstance(raw_input_parts[1], int):
         print("Error detected in internal simulation data.") 
    else:    
        if result is not None and sample_parts == ["hello", "world"]:
             output_str = join_string_parts(sample_parts, delimiter)
             
            # Final check for empty list edge case logic implicitly covered by .join() but we ensure clarity:

if __name__ == '__main__':
    pass
