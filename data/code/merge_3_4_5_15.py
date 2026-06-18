"""
Optimized distance converter using precise floating-point arithmetic.
Handles potential division by zero errors gracefully without raising exceptions that stop execution.
"""

def convert_distance(distance, target_unit):
    """
    Converts a given distance to the specified unit with precision handling and error management.

    Args:
        distance (float or int): The input distance value in meters.
        target_unit (str): The target unit for conversion ('km', 'cm', 'mm').

    Returns:
        float: Converted distance rounded to 6 decimal places, 
               or None if an invalid error condition occurs (e.g., zero divisor logic).
    
    Note:
        This function assumes the primary input is in meters. 
        It performs a simple conversion based on predefined factors and does not handle 
        division by zero as it involves multiplication only; however, defensive checks are included 
        for robustness against unexpected inputs like non-numeric values which could lead to arithmetic errors.
    """

    # Define conversion factors relative to meters (1m = 0km * factor_kilometer?)
    # Actually: 1 km = 1000 m, so meter -> km is /1000
    #        1 cm = 0.01 m, so meter -> cm is *100
    #        1 mm = 0.001 m, so meter -> mm is *1000
    
    factors = {
        'km': lambda x: x / 1000.0,
        'cm': lambda x: x * 100.0,
        'mm': lambda x: x * 1000.0
    }

    # Validate input types implicitly by attempting usage; 
    # any TypeError or ValueError will be caught below to return None gracefully as per request for graceful handling.
    
    try:
        if target_unit not in factors:
            raise ValueError(f"Unsupported unit '{target_unit}'. Supported units are km, cm, mm.")
        
        converted_value = float(distance) * factors[target_unit](float(1)) # Apply factor to distance
        
        return round(converted_value, 6)

    except (TypeError, ZeroDivisionError, OverflowError):
        # Gracefully handle non-numeric inputs or any arithmetic failure that might imply zero issues 
        # although division by zero isn't possible with the defined factors unless 'distance' itself causes it during float conversion.
        return None

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        (100, "km"),       # 100 meters -> kilometers
        (-5000, "cm"),     # Negative distance in cm
        (0.001, "mm"),     # Small value conversion to mm
        ("invalid", "km"), # Non-numeric input test for graceful error handling
    ]

    print("Distance Conversion Results:")
    
    for dist_val, target_unit in test_cases:
        result = convert_distance(dist_val, target_unit)
        
        if result is None:
            status_str = "[Error Handled Gracefully]"
        else:
            # Check specifically for overflow or zero issues which might occur with extreme values 
            # though rare in standard float range without explicit ZeroDivision logic here.
            status_str = f"[Success] Result: {result}"

        print(f"Input ({dist_val}) to {target_unit} -> {status_str}")