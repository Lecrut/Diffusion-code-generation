def validate_input(input_str):
    """Attempts to convert input string to a float."""
    try:
        return float(input_str)
    except ValueError:
        raise ValueError(f"Invalid number format: '{input_str}'")

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without user interaction or command-line arguments.
    first_number = validate_input("10")
    second_number = validate_input("-5")

    if first_number > second_number:
        print(f"{first_number} is greater than {second_number}")
    else:
        print(f"{first_number} is not greater than {second_number}")