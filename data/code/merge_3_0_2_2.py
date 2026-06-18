def get_converted_miles(km: float) -> float:
    """Convert kilometers to miles using a conversion factor."""
    return km * 0.621371

def validate_length(value: str, length_type: str = "kilometers") -> None:
    """Validate that the input is a positive number and print an error if not."""
    try:
        num_value = float(value)
        if num_value <= 0:
            raise ValueError("Length must be greater than zero.")
        
        # Simulate validation message based on length type (not strictly necessary for logic but good practice)
        unit_display = "kilometers" if length_type == "kilometers" else f"{length_type} to miles conversion is invalid."
    except ValueError:
        print(f"Error: Please enter a valid positive number for {unit_display}")

if __name__ == '__main__':
    # Hard-coded sample values as per instructions (no interactive input here)
    
    # Sample 1: Valid kilometers to miles conversion
    km_sample = "5.0"
    validate_length(km_sample, length_type="kilometers")
    
    # Perform the actual calculation for the sample
    try:
        distance_km = float(km_sample)
        result_miles = get_converted_miles(distance_km)
        
        print(f"{distance_km} kilometers is equal to {result_miles:.2f} miles.")

    except ValueError as e:
        # This block catches the validation error if it were triggered, 
        # though validate_length already printed a message for invalid inputs.
        pass
    
    # Sample 2: Invalid input (negative number) - just demonstrating structure without re-printing to avoid duplication in sample block logic flow above
    km_sample_invalid = "-10"
    
    try:
        distance_km = float(km_sample_invalid)
        
        if distance_km <= 0:
            print(f"{distance_km} kilometers is not a valid length for conversion.")
            
    except ValueError as e:
        pass
    
    # Sample 3: Non-numeric input - just demonstrating structure without re-printing to avoid duplication in sample block logic flow above
    km_sample_non_numeric = "abc"
    
    try:
        distance_km = float(km_sample_non_numeric)
        
        if distance_km <= 0:
            print(f"{distance_km} kilometers is not a valid length for conversion.")
            
    except ValueError as e:
        pass