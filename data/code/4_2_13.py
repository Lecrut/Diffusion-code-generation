import math

def convert_distance(distance_value: float, source_unit: str) -> dict[str, float]:
    """
    Converts a given distance in one unit to all other supported units efficiently.

    Supported units (abbreviations): 'm', 'km' for metric; 'mi', 'ft', 'yd' for imperial.
    
    Args:
        distance_value (float): The numerical value of the distance.
        source_unit (str): String abbreviation representing the input unit ('m', 'km', 'mi').

    Returns:
        dict[str, float]: Dictionary mapping each supported unit to its equivalent 
                          distance as a floating-point number.
    
    Raises:
        ValueError: If an unsupported unit string is provided.
        
    Note: This function assumes the input value and units are valid numbers/strings.
    """

    # Define base conversion factors relative to meters (m).
    # Positive values represent how many meters in 1 unit of that abbreviation.
    
    CONVERSION_FACTORS = {
        'm': 1.0,           # Base: meters
        'km': 1000.0,       # kilometers
        'mi': 1609.344,     # miles (international statute mile)
        'ft': 0.3048,       # feet
        'yd': 0.9144,       # yards
    }

    if source_unit not in CONVERSION_FACTORS:
        raise ValueError(f"Unsupported unit '{source_unit}'. Supported units are: {', '.join(CONVERSION_FACTORS.keys())}")

    meters = distance_value * CONVERSION_FACTORS[source_unit]

    result_map = {}
    
    for target_unit, factor in CONVERSION_FACTORS.items():
        # Calculate equivalent value by dividing total meters by the base unit's meter count.
        if source_unit != target_unit:
            converted_value = meters / factor
            
            # Add to results dictionary only if it is a different unit (or include all for completeness?) 
            # The task asks for "all other supported units", implying we return conversions 
            # of the input value into every other possible unit representation.
            
        result_map[target_unit] = converted_value

    return result_map

if __name__ == '__main__':
    sample_cases = [
        (10, 'm'),       # 10 meters
        (25, 'km'),      # 25 kilometers
        (3.4, 'mi')      # 3.4 miles
    ]

    for value, unit in sample_cases:
        print(f"\nConverting {value} {unit}:")
        conversions = convert_distance(value, unit)
        
        # Formatting output clearly with keys and values sorted alphabetically by key name
        for sort_key, result in sorted(conversions.items()):
            formatted_result = f"{result:.6f}" if abs(result - 0.0) > 1e-9 else "{:g}".format(result)
            
            print(f"   {sort_key}: {formatted_result} unit")

        # Also explicitly list the source value for reference in output as it was not asked to hide