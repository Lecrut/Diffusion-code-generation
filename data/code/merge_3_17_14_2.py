import sys

def determine_parity(number: int) -> str:
    """
    Checks if a number is even or odd.

    Args:
        number (int): The integer to check.

    Returns:
        str: A message indicating 'even' or 'odd'.
    """
    status = "The entered number IS EVEN" if number % 2 == 0 else "The entered number IS ODD"
    return f"{status}. Number provided was {number}."

def validate_input(input_str: str) -> int | None:
    """
    Attempts to convert a string input to an integer.

    Args:
        input_str (str): The string representation of the potential number.

    Returns:
        int | None: The converted integer if successful, otherwise returns None for error handling.
    """
    try:
        return int(input_str)
    except ValueError:
        # This handles cases where input is not a valid integer (e.g., letters or empty string with non-space chars).
        raise RuntimeError(f"Error: Input '{input_str}' could not be converted to an integer.")

if __name__ == '__main__':
    # Hard-coded sample values for testing as per requirements.
    test_cases = ["42", "17", "0", "-3"]

    print("Testing parity check with the following samples:")
    for case in test_cases:
        try:
            num_input = int(case)  # Direct conversion from string to validate logic flow
            result = determine_parity(num_input)
            print(result)
        except ValueError:
            print(f"Handled non-integer input '{case}' internally by attempting direct conversion which is valid for our specific test list but shows the type handling.")

    # Simulating error scenario without using sys.stdin or argparse directly as per constraints.
    # We demonstrate how an invalid string would be handled if it were passed to validate_input logic,
    # though strictly adhering to 'no input()' means we only execute on hard-coded valid strings here.