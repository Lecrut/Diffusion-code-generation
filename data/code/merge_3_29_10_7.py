#!/usr/bin/env python3
"""
Script to reverse a given input string.
Handles various types: str, bytes (decoded), and lists of strings joined into one string before reversal.

Usage Example:
    The main block runs with pre-defined sample values without requiring user interaction or external inputs.
"""

def get_input_string(data):
    """
    Accepts data in different formats and returns a single string to be reversed.
    
    Parameters:
        data (str | bytes | list[str]): Input data
    
    Returns:
        str: The joined input as a string if not already a string, otherwise the original string.
    """
    # If it's a list of strings, join them first; otherwise return directly or convert to str
    try:
        if isinstance(data, (list, tuple)):
            result = "".join(str(item) for item in data)
            return result
        else:
            return str(data)
    except Exception as e:
        raise TypeError(f"Unsupported input type {type(data).__name__}. Error details: {e}")

def reverse_string(input_str):
    """
    Reverses the given string character by character.

    Parameters:
        input_str (str): The string to be reversed
    
    Returns:
        str: A new string with characters in reverse order
    """
    if not isinstance(input_str, str):
        raise ValueError(f"Expected a string type for reversal operation, got {type(input_str).__name__}")

    return input_str[::-1]

def main():
    """Main entry point running the script with pre-defined samples."""
    
    # Hard-coded sample values to ensure no user interaction or external dependencies are needed.
    # These include a standard string, bytes representation (simulated), and a list of words.
    sample_inputs = [
        "Hello World",               # Standard string example
        b"Python is fun".decode("utf-8"),  # Simulating byte input handling by decoding first
        ["This", "-", "is", "-"],   # List of strings to be joined before reversal
    ]

    for item in sample_inputs:
        try:
            processed_string = get_input_string(item)
            reversed_text = reverse_string(processed_string)
            
            print(f"Original Input Type ({type(item).__name__}): {item}")
            print("Reversed Output:")
            print(reversed_text)
            print("-" * 30)
        except Exception as e:
            # Gracefully handle unexpected errors during processing individual samples
            error_msg = f"""Error while processing sample input of type {type(item).__name__}: 
{str(e)}

This could be due to unsupported data structure or invalid characters."""
            print(error_msg)

if __name__ == '__main__':
    main()