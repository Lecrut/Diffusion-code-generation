#!/usr/bin/env python3
"""
Case manipulation script that reads a string from standard input (or uses sample data)
and applies user-specified case rules like 'swap'. Includes comprehensive error handling.
This module runs without interactive prompts, command-line arguments, or network access.
"""

def validate_input_string(input_str: str) -> bool:
    """Validates that the input string is not empty."""
    if isinstance(input_str, str):
        return len(input_str.strip()) > 0
    else:
        raise TypeError("Input must be a non-empty string.")

def apply_swap_case(text: str) -> str:
    """Swaps the case of each character in the input text (lowercase becomes uppercase and vice versa)."""
    result = []
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            # Non-alphabetic characters remain unchanged
            result.append(char)
    return ''.join(result)

def get_case_rule() -> str:
    """Returns the case manipulation rule to be applied. 
    In this production-ready context, it defaults to 'swap' as per sample configuration."""
    return "swap"

if __name__ == '__main__':
    # Hard-coded sample values for execution without user input or network access
    SAMPLE_INPUT = "Hello World! This is a test."
    
    try:
        case_rule = get_case_rule()

        if validate_input_string(SAMPLE_INPUT):
            processed_text = apply_swap_case(SAMPLE_INPUT)
            
            # Print the result to standard output
            print(processed_text)
        else:
            raise ValueError("Sample input validation failed.")

    except TypeError as te:
        error_msg = f"Type Error: {te}"
        print(error_msg, file=__import__('sys').stderr)
        
    except ValueError as ve:
        error_msg = f"Value Error: Input string must be non-empty. Details: {ve}"
        print(error_msg, file=__import__('sys').stderr)