import sys

def read_positive_float(text):
    """Attempt to convert a text string to a positive float."""
    try:
        value = float(text)
        if value <= 0:
            raise ValueError("Input must be a positive number.")
        return value
    except (ValueError, TypeError):
        raise

def calculate_ratio(num1_str, num2_str):
    """Calculate the ratio of two length measurements."""
    num1 = read_positive_float(num1_str)
    num2 = read_positive_float(num2_str)
    
    if num2 == 0:
        # Handle division by zero gracefully as a special case or let math domain error occur.
        # For this task, we will raise an informative ValueError for clarity on invalid inputs.
        return None
    
    result = num1 / num2
    return result

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or network access.
    measurement_a_str = "50"   # Sample length 1: 50 units
    measurement_b_str = "10"   # Sample length 2: 10 units
    
    try:
        ratio_value = calculate_ratio(measurement_a_str, measurement_b_str)
        
        if ratio_value is not None and math.isfinite(ratio_value):
            print(f"The ratio of {measurement_a_str} to {measurement_b_str} is {ratio_value:.2f}")
        else:
            # This block handles cases where calculation failed or returned invalid results.
            print("An error occurred during ratio calculation.")
    except ValueError as e:
        # Gracefully handle potential ValueErrors raised by the validation logic.
        print(f"Input validation error: {e}", file=sys.stderr)