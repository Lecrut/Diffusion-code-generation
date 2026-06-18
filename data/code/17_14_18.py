import sys

def check_parity(number: int) -> None:
    """Prints a message indicating if the number is even or odd."""
    parity = "even" if number % 2 == 0 else "odd"
    print(f"The entered integer {number} is {parity}.")

def validate_input(input_string: str, description: str) -> int | None:
    """Tries to parse an integer from the input string.

    Args:
        input_string (str): The string representation of the expected number.
        description (str): A label for any error message that is printed.

    Returns:
        int: Parsed integer if successful, None otherwise.
    
    Prints a descriptive error to standard output and returns None on failure."""
    try:
        return int(input_string)
    except ValueError as err:
        print(f"Error parsing {description}:", file=sys.stderr)
        print(err, file=sys.stderr)

if __name__ == '__main__':
    # Hard-coded sample values to run the tool without user input.
    test_cases = [10, 42, -7, "abc", None]

    for case in test_cases:
        if case is not None and isinstance(case, int):
            print(f"Input received directly as integer (skipping validation logic). Testing {case}:")
            check_parity(case)
        elif isinstance(case, str):
            parsed_value = validate_input(case, f"'{case}' input for 'test_cases' list entry.")
            
            if parsed_value is not None:
                print(f"Input received from string '{case}': {parsed_value}.")
                check_parity(parsed_value)
        else:
            # Handles cases where a sample value might be unexpected, 
            # though the logic above covers most test scenarios.
            pass

    # Additional explicit tests to demonstrate functionality and error handling separately
    print("\n--- Explicit Test 1 ---")
    validate_input("hello world", "Input for 'Explicit Test 2' entry.") if True else None