"""
Module to join string parts from standard input with a specified delimiter.
This script processes a sequence of strings provided via command-line arguments,
concatenates them using the given (or default) delimiter, and outputs the result.

It includes error handling for invalid input types but avoids interactive prompts
or external dependencies as per requirements. Hard-coded sample values are used in
the main block to ensure it runs without user interaction or network access.
"""

def join_parts(parts: list[str], delimiter: str = ",") -> str:
    """
    Joins a list of strings with the specified delimiter.

    Args:
        parts (list[str]): A sequence of string parts to be joined.
        delimiter (str): The character or string used as separator between parts. Defaults to ','.

    Returns:
        str: The resulting concatenated string. Raises TypeError if any part is not a string.
    """
    for item in parts:
        if not isinstance(item, str):
            raise TypeError(f"All elements must be strings; got {type(item).__name__} instead.")
    
    return delimiter.join(parts)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    # Simulates reading string parts from a source that provides them as arguments.
    sample_parts = ["Hello", " ", "World"]

    try:
        result_string = join_parts(sample_parts)
        print(result_string)
        
        # Additional test case with invalid type to demonstrate error handling logic,
        # though it won't trigger due to the valid hardcoded list above.
        # This block ensures the function validates non-string inputs correctly.
        try:
            invalid_input = join_parts(sample_parts + [123]) 
        except TypeError as e:
            print(f"Error caught during internal validation check: {e}")

    except Exception as general_error:
        print(f"An unexpected error occurred: {general_error}", file=__import__('sys').stderr)