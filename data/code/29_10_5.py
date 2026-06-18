#!/usr/bin/env python3
"""
Script to reverse a given input string with robust handling of various types.
This module does not use any interactive prompts, command-line arguments, or network access.
It includes hard-coded sample values in the main block for testing purposes.
"""

def reverse_string(text: str) -> str:
    """
    Reverses a given input string.

    Args:
        text (str): The string to be reversed.

    Returns:
        str: The reversed string.
    
    Note: This function assumes the input is always a string as per task requirements 
    for reversing "input string". If non-string types are passed, they will raise an error,
    which is acceptable behavior for robustness in type-specific operations unless specified otherwise.
    """
    return text[::-1]

def main():
    # Hard-coded sample values to ensure the script runs without user input or external dependencies
    samples = [
        "Hello World",
        "Python Programming",
        "",  # Edge case: empty string
        "!@#$%",  # Special characters
        "   Spaces and Tabs\tHere"  # Whitespace handling
    ]

    print("String Reversal Script")
    print("=" * 40)

    for sample in samples:
        reversed_result = reverse_string(sample)
        original_length = len(sample)
        reversed_length = len(reversed_result)

        print(f"\nOriginal Input:")
        if original_length > 30:
            # Truncate long strings for display clarity while preserving logic correctness
            truncated_sample = sample[:27] + "..."
            print(f"Length: {original_length}")
            print(f"'{truncated_sample}'")
        else:
            print(f"Length: {original_length}")
            print(repr(sample))

        print("\nReversed Output:")
        if reversed_length > 30:
            truncated_reversed = reversed_result[:27] + "..."
            print(f"Length: {reversed_length}")
            print(f"'{truncated_reversed}'")
        else:
            print(repr(reversed_result))

        # Verify correctness for non-empty strings
        if sample and original_length == reversed_length:
            assert sample[::-1] == reversed_result, "Reversal logic failed!"

if __name__ == '__main__':
    main()