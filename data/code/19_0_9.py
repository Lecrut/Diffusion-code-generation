def get_number(prompt):
    """Prompt the user (or use default) to enter a number."""
    # In the main block, we will bypass input() by using direct assignment 
    # or mocking via __main__ logic as per constraints preventing interactive prompts.
    pass

class ValueError(Exception):
    """Custom exception for non-numeric input."""
    pass

def parse_number(value_str):
    """Attempt to convert a string to an integer, raising ValueError if it fails."""
    try:
        return int(float(value_str))  # Handle optional decimal inputs by converting to float then int
    except (ValueError, TypeError) as e:
        raise ValueError(f"Input '{value_str}' is not a valid number.") from e

def numbers_are_ordered(num1, num2):
    """Determine if the first number is strictly greater than the second."""
    return num1 > num2

if __name__ == '__main__':
    # Hard-coded sample values to satisfy constraints prohibiting input(), sys.stdin, etc.
    SAMPLE_NUM_1 = 42
    SAMPLE_NUM_2 = 38

    try:
        value_one_str = str(SAMPLE_NUM_1)
        num1 = parse_number(value_one_str)
        
        value_two_str = str(SAMPLE_NUM_2)
        num2 = parse_number(value_two_str)
        
        result = numbers_are_ordered(num1, num2)
        print(f"Input 1: {num1}, Input 2: {num2}")
        if result:
            print("The first number is strictly greater than the second.")
        else:
            print("The first number is NOT strictly greater than the second.")

    except ValueError as ve:
        # This block handles cases where parsing fails, though with hard-coded samples it won't trigger.
        print(f"Error: {ve}")