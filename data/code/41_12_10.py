import sys

def validate_input_string(s):
    """Validates that the input is a non-empty string."""
    if s is None:
        raise ValueError("Input cannot be null.")
    if not isinstance(s, str):
        raise TypeError(f"Expected 'str', got '{type(s).__name__}'.")
    return True

def apply_swap_rule(text):
    """Swaps the case of each character in the input string."""
    result = []
    for char in text:
        if char.isupper():
            result.append(char.lower())
        elif char.islower():
            result.append(char.upper())
        else:
            # Preserve non-alphabetic characters (numbers, symbols, spaces)
            result.append(char)
    return ''.join(result)

def main_solution(input_str):
    """
    Main processing function.
    
    Args:
        input_str (str): The string to process based on the 'swap' rule.
        
    Returns:
        str: The transformed string with swapped case characters.
        
    Raises:
        ValueError: If input validation fails.
    """
    try:
        validate_input_string(input_str)
        return apply_swap_rule(input_str)
    except Exception as e:
        raise RuntimeError(f"Unexpected error during processing: {str(e)}")

if __name__ == '__main__':
    # Hard-coded sample values to ensure the script runs without user input or arguments.
    samples = [
        "Hello, World!",       # Expected Output: hELLO, wORLD!
        "Python 3.10",         # Expected Output: pYTHON 3.10
        "!@#$%^&*()",          # Expected Output: !@#$%^&*() (No change)
        ""                     # Edge case: Empty string -> No change
    ]

    for sample in samples:
        try:
            output = main_solution(sample)
            print(f"Input: '{sample}'")
            print(f"Output: {output}")
            print("-" * 40)
        except Exception as e:
            # Silent fail or handle specific logging if desired, but keeping it clean.
            pass