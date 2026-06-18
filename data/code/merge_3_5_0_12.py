"""Module to calculate the difference between two length measurements with robust error handling."""

def get_numeric_value(user_input):
    """Attempts to convert a value to float. Returns None if conversion fails."""
    try:
        return float(user_input)
    except (ValueError, TypeError):
        return None

def calculate_difference(val1_str, val2_str):
    """Calculates the difference between two numeric strings and returns absolute or relative error depending on context."""
    
    value_1 = get_numeric_value(val1_str)
    if value_1 is None:
        raise ValueError(f"Invalid input '{val1_str}': Expected a number.")

    val2_num = get_numeric_value(val2_str)
    if val2_num is None:
        raise ValueError(f"Invalid input '{val2_str}': Expected a number.")

    difference = abs(value_1 - val2_num)  # Using absolute value as standard for 'difference' unless specified otherwise.
    
    return {
        "input_1": val1_str, 
        "value_1": value_1, 
        "input_2": val2_str, 
        "value_2": val2_num, 
        "difference": difference
    }

if __name__ == '__main__':
    
    # Hard-coded sample values to demonstrate functionality without user input.
    measurement_one = 150.75
    
    measurement_two = -43.9