def get_even_odd_status(number):
    """Determine if a number is even or odd."""
    return "even" if number % 2 == 0 else "odd"

def validate_input(input_str, error_msg="Invalid input: Please enter an integer."):
    """Validate that the input string can be converted to an integer."""
    try:
        int_value = int(input_str)
        return True, int_value
    except ValueError:
        print(error_msg)
        return False, None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or arguments.
    test_cases = [10, 25, "abc", -4]

    for case in test_cases:
        is_valid, number_value = validate_input(case)

        if is_valid and number_value is not None:
            status_message = get_even_odd_status(number_value)
            print(f"The entered number {number_value} is a {status_message}.")