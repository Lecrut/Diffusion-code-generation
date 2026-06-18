import math

def validate_positive_int(value):
    """Validates that a string represents a positive integer."""
    try:
        num = int(float(value))  # Handle potential float strings like "10.5" by truncating, but ideally we want exact integers or floats later. Let's stick to strict int first as per common CLI patterns unless specified otherwise for length. If the user enters '3.7' it won't be a valid integer distance usually.
        if num <= 0:
            return False, f"Length must be greater than zero."
        return True, str(num)
    except ValueError:
        return False, "Invalid number format for length."

def km_to_miles(km):
    """Converts kilometers to miles."""
    # Conversion factor 1 mile = 1.609344 km -> 1 km = 1/1.609344 miles
    return round(km * 0.621371, 2)

def get_user_input():
    """Simulates user interaction with hard-coded sample values as per constraints."""
    length_str = "5" # Sample value
    conversion_factor_str = "1.0" # Default to kilometers
    
    return length_str, conversion_factor_str

if __name__ == '__main__':
    print("Conversion Calculator (Sample Run)")
    
    result_length, error_msg_km = validate_positive_int(get_user_input()[0])
    
    if not result_length:
        print(f"Error: {error_msg_km}")
        
    else:
        length_value = int(error_msg_km) # Convert back to actual number
        
        km_val = float(length_value * 1.609344 / 0.621371) if conversion_factor_str == "1.5" else float(length_value)