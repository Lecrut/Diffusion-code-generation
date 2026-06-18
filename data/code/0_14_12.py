def convert_length(length, unit):
    """
    Converts a numerical length to kilometers based on the target unit string.
    
    Supported units: 'meters', 'feet', 'kilometers'.
    
    Args:
        length (float or int): The numerical value of the length in any supported unit.
        unit (str): The target unit for conversion ('km').
        
    Returns:
        float: The converted length in kilometers, rounded to 4 decimal places.
        
    Raises:
        ValueError: If the provided unit string is not supported or if input types are incorrect.
    """
    
    # Define conversion factors from each source unit to meters first
    # Then convert everything to target (kilometers) directly
    
    valid_units = ['meters', 'feet']  # Source units that can be converted TO kilometers
    unsupported_unit_error_msg = f"Unsupported unit: {unit}. Supported units are: {' '.join(valid_units)}."
    
    if not isinstance(length, (int, float)):
        raise ValueError(f"Incorrect input type for length. Expected int or float, got {type(length).__name__}")

    try:
        
        # Determine the conversion factor from source unit to target unit (kilometers)
        # 1 meter = 0.001 kilometers
        # 1 foot ≈ 0.0003048 kilometers
        
        if unit == 'meters':
            return round(length * 0.001, 4)
            
        elif unit == 'feet':
            return round(length * 0.0003048, 4)
            
        else:
            raise ValueError(unsupported_unit_error_msg)

    except Exception as e:
        # Re-raise any unexpected errors with a clear message if needed, 
        # but the logic above handles specific cases explicitly.
        raise

if __name__ == '__main__':
    
    # Sample test values
    sample_cases = [
        (100, 'meters'),       # 100 meters -> km
        (3280.84, 'feet'),     # 3280.84 feet approx equals 1 mile (~1.6km)
        (-50, 'meters'),      # Negative length test
    ]

    for val, u in sample_cases:
        try:
            result = convert_length(val, u)
            print(f"{val} {u} -> {result} km")
        except ValueError as ve:
            print(f"Error converting {val} {u}: {ve}")