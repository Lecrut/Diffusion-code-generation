import sys

def parse_number(user_input):
    """
    Attempts to convert a string input into an integer (float).
    
    Args:
        user_input (str): The raw input from the console or source.
        
    Returns:
        float: Parsed numeric value if successful, None otherwise.
    """
    try:
        return int(float(user_input))  # Supports inputs like '3.5' by converting to float then casting back for consistency with typical number comparison tasks in text prompts, but primarily handles integers and decimals gracefully returning the parsed float result
    except ValueError:
        print(f"Error: Unable to convert '{user_input}' into a valid numeric value.")
        return None

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes without any user interaction, command-line arguments, or network access.
    num1_str = "50"      # Simulated console input as string '50'
    num2_str = "-37"     # Simulated console input as string '-37'

    # Parse the simulated inputs into numbers
    number_one = parse_number(num1_str)
    
    if not isinstance(number_one, int):
        print("Parsing failed for first value. Exiting.")
        sys.exit(1)