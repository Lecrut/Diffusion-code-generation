import sys

def parse_integer(input_str):
    """Attempts to convert a string to an integer, raising ValueError if it fails."""
    try:
        return int(input_str)
    except ValueError as e:
        raise RuntimeError(f"Invalid input '{input_str}': {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction or external dependencies.
    first_number = "10"
    second_number = "20"

    try:
        num_one = parse_integer(first_number)
        num_two = parse_integer(second_number)
        
        if num_one == num_two:
            print(f"The numbers {first_number} and {second_number} are equal.")
        else:
            print(f"The numbers {first_number} and {second_number} are not equal.")

    except (RuntimeError, TypeError) as error:
        # Handles cases where inputs cannot be parsed as integers.
        print("Error occurred while processing input:", str(error))