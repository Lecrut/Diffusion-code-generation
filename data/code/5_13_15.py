def validate_numeric_input(user_value):
    """Attempts to convert a string input to a float."""
    try:
        return float(user_value)
    except ValueError:
        raise ValueError(f"Invalid numeric value: '{user_value}'")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user interaction or CLI args needed)
    measurement_a = 10.5
    measurement_b = 23.7

    print("--- Detailed Measurement Comparison ---\n")
    
    try:
        value_a = validate_numeric_input(measurement_a)
        value_b = validate_numeric_input(measurement_b)
        
        difference = abs(value_a - value_b)
        
        # Formatting output to two decimal places for clarity
        formatted_diff = f"{difference:.2f}"

        print(f"Value A: {value_a}")
        print(f"Value B: {value_b}")
        print("-" * 30)
        print(f"Difference (|A - B|): {formatted_diff}")
        
    except ValueError as e:
        # Since these are hard-coded, this block technically won't trigger on valid floats,
        # but it demonstrates the validation logic if invalid data were passed.
        print(f"Error during calculation: {e}")