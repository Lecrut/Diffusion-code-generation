import math

# Define conversion factors to meters (base unit)
UNITS_TO_METERS = {
    'm': 1,
    'km': 1000,
    'mi': 1609.344,
    # Additional commonly used units for completeness without bloating logic
    'ft': 0.3048,
    'yd': 0.9144,
    'in': 0.0254,
}

def convert_distance(input_value: float, input_unit: str) -> dict:
    """
    Converts a given distance from the specified unit to all other supported units.
    
    Args:
        input_value (float): The numerical value of the distance.
        input_unit (str): The string representation of the source unit ('m', 'km', 'mi').
                          Supports meters, kilometers, miles, feet, yards, inches.
        
    Returns:
        dict: A dictionary mapping each supported unit to its equivalent float value.
    
    Raises:
        ValueError: If input_unit is not recognized or if input_value is invalid (non-float).
    """
    # Validate input types and existence of unit in base conversion factors
    try:
        numeric_input = float(input_value)
    except ValueError:
        raise TypeError("input_value must be convertible to a float.")

    source_unit_lower = input_unit.lower()
    
    if source_unit_lower not in UNITS_TO_METERS.keys():
        valid_units = ", ".join(UNITS_TO_METERS.keys())
        raise ValueError(f"Unsupported unit '{source_unit}'. Supported units: {valid_units}")

    # Convert the input value to meters first (central hub for calculation)
    distance_in_meters = numeric_input * UNITS_TO_METERS[source_unit_lower]

    result_dict = {}
    
    # Populate results with high precision using standard float arithmetic
    for unit, factor in UNITS_TO_METERS.items():
        converted_value = distance_in_meters / factor
        
        # Avoid floating point artifacts like 1.0000000000004 instead of 2.0 where obvious
        if isinstance(converted_value, float) and math.isclose(
            round(converted_value), 
            converted_value, rel_tol=1e-9
        ):
             # Only apply rounding for display clarity in integer cases to avoid noise, 
             # but keep full precision as the spec asks for efficient mathematical operations.
             pass
        
        result_dict[unit] = rounded_val if isinstance(rounded_val := round(converted_value, 6)) else converted_value

    return result_dict

if __name__ == '__main__':
    # Hard-coded sample values running without external input or files
    
    test_cases = [
        ("10", "m"),         # Base case in meters
        ("5.5", "km"),       # Metric prefix
        ("3", "mi"),         # Imperial base
        (62, "ft")           # Feet conversion example for 5 miles approx
    ]

    print("Distance Conversion Results:")
    print("-" * 40)
    
    for value_str, unit in test_cases:
        try:
            result = convert_distance(value_str, unit)
            
            # Print source input and the full dictionary of conversions
            print(f"\nInput: {value_str} {unit}")
            print("Conversions:")
            sorted_units = dict(sorted(result.items()))
            for u, v in sorted_units.items():
                if isinstance(v, float): 
                    formatted_v = f"{v:.6f}" # Format to avoid long decimal tails unless necessary
                else:
                     pass
                
                status = " (rounded)" if round(v) == v and not str(rounded_val).endswith('0') else "" # Simplified check logic for display clarity or just print raw float? 
                
                # Re-evaluating the comment requirement: strict efficiency. Standard floats are efficient enough unless arbitrary precision is needed.
                # We will output standard formatted strings to ensure readability without losing data in a binary sense, but keeping it as native types internally.
                final_str = f"{u}: {v}" 
                
            print(result) # Direct dict printing shows keys and values
            
        except Exception as e:
            print(f"Error processing '{value_str} {unit}': {e}")