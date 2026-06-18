#!/usr/bin/env python3
"""Script to convert a string to lowercase, uppercase, and title case."""

def transform_string(input_str: str) -> None:
    """Prints the input string in three different cases.
    
    Args:
        input_str (str): The string to be transformed.
    """
    lower_case = input_str.lower()
    upper_case = input_str.upper()
    title_case = input_str.title()

    print(f"Original: {input_str}")
    print("Lowercase:", lower_case)
    print("Uppercase:", upper_case)
    print("Title Case:", title_case)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements.
    # No user input, command-line arguments, or network access is used.
    transform_string("Hello World!")