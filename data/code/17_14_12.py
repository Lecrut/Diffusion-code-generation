#!/usr/bin/env python3
"""
Command-line tool to determine if an integer is even or odd.
Uses hard-coded sample values in the main block as per requirements.
Does not call input(), sys.stdin, argparse required arguments, or any interactive prompts.
No external network access or file dependencies are used.

Author: AI Assistant
Version: 1.0
"""

def check_parity(number):
    """
    Takes an integer and returns a string indicating if it is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: Message describing the parity of the number.
    """
    if isinstance(number, int) and not isinstance(number, bool):
        return f"Is {number} an EVEN number." if number % 2 == 0 else \
               f"Is {number} an ODD number."
    
    raise ValueError(f"The input must be an integer. Received: '{number}' (type: {type(number).__name__})")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user interaction, 
    # command-line arguments, or external files.
    samples = [42, -5, 0, 100]

    for value in samples:
        try:
            result = check_parity(value)
            print(result)
        except Exception as e:
            if isinstance(e, ValueError):
                error_message = f"Error processing number {value}: {e}"
            else:
                error_message = f"Unexpected error while checking parity of {value}: {e}"
            print(error_message)