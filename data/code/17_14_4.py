import sys

def check_parity(number: int) -> str:
    """
    Returns a message indicating whether the number is even or odd.
    
    Args:
        number (int): The integer to check.
        
    Returns:
        str: A descriptive string about the parity of the number.
    """
    if number % 2 == 0:
        return f"The number {number} is even."
    else:
        return f"The number {number} is odd."

def validate_input(input_str: str) -> int | None:
    """
    Attempts to convert the input string to an integer.
    
    Args:
        input_str (str): The raw input from standard input or sample data.
        
    Returns:
        int | None: The parsed integer if successful, otherwise None.
    """
    try:
        return int(input_str)
    except ValueError:
        print("Error: Invalid input. Please enter a valid integer.")
        sys.exit(1)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user interaction, arguments, or files.
    samples = ["42", "73", "-8"]

    for sample in samples:
        input_value = validate_input(sample)
        
        if input_value is not None:
            result_message = check_parity(input_value)
            print(result_message)