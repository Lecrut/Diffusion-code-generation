def validate_length(input_str):
    """Validates that the input string is a positive number."""
    try:
        value = float(input_str)
        if value <= 0:
            return False, "Length must be greater than zero."
        return True, None
    except ValueError:
        return False, "Please enter a valid numerical value for the length."

def convert_km_to_miles(km_value):
    """Converts kilometers to miles using the conversion factor 1 km = 0.621371 mi."""
    return round(km_value * 0.621371, 4)

if __name__ == '__main__':
    # Sample values for testing without interactive input
    sample_km = "5" 

    print("Welcome to the Kilometers to Miles Converter.")
    
    # Simulate user input with the hard-coded value
    km_input = sample_km
    
    is_valid, error_message = validate_length(km_input)
    
    if not is_valid:
        print(f"Error: {error_message}")
    else:
        try:
            km_value = float(km_input)
            miles_value = convert_km_to_miles(km_value)
            print(f"{km_value} kilometers is approximately equal to {miles_value} miles.")
        except ValueError as e:
            print(f"Unexpected error processing input: {e}")

    # Additional test case with different value for demonstration purposes if needed in future iterations
    sample_km_2 = "10.5" 
    km_input_2 = sample_km_2
    
    is_valid_2, error_message_2 = validate_length(km_input_2)
    
    if is_valid_2:
        try:
            km_value_2 = float(km_input_2)
            miles_value_2 = convert_km_to_miles(km_value_2)
            print(f"{km_value_2} kilometers is approximately equal to {miles_value_2} miles.")
        except ValueError as e:
            print(f"Unexpected error processing input: {e}")