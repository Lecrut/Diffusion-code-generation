import math

def convert_distance(distance: float, target_unit: str) -> float | None:
    """
    Converts a distance value to the specified unit using precise floating-point arithmetic.
    
    Supported units (input): meters ('m'), kilometers ('km'), miles ('mi').
    Returns the converted value in the target unit or None if conversion is invalid.
    
    Handles potential division by zero gracefully and validates input types.
    
    Args:
        distance (float): The numerical value of the distance to convert.
        target_unit (str): The desired output unit ('m', 'km', 'mi').
        
    Returns:
        float | None: Converted distance in the target unit, or None if conversion fails.
    """
    
    # Define base units relative to meters for consistent calculation
    BASE_METERS = 1.0
    
    # Conversion factors from each input unit to meters (to avoid repeated division by zero)
    UNIT_TO_METERS = {
        'm': BASE_METERS,
        'km': 1000.0 * BASE_METERS,
        'mi': 1609.344 * BASE_METERS
    }

    # Validate input types and handle division by zero logic implicitly via dictionary lookup
    
    if not isinstance(distance, (int, float)):
        return None
        
    if distance != distance:  # Check for NaN using IEEE 754 standard behavior
        return None
        
    target_unit_lower = str(target_unit).strip().lower()
    
    try:
        meters_per_input_unit = UNIT_TO_METERS.get('m')
        
        if not isinstance(meters_per_input_unit, float):
            return None
            
        # Convert input to meters first (avoids direct division by zero on target unit)
        distance_in_meters = distance * meters_per_input_unit
        
    except ZeroDivisionError:
        return None
    
    try:
        meters_per_target_unit = UNIT_TO_METERS.get(target_unit_lower, 0.0)
        
        if not isinstance(meters_per_target_unit, float):
            return None
            
        # Perform final conversion to target unit (safe from division by zero due to validation above)
        converted_value = distance_in_meters / meters_per_target_unit
        
    except ZeroDivisionError:
        return None
    
    return converted_value

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    test_cases = [
        (100, 'm'),           # 100 meters to meters -> 100.0
        (5, 'km'),            # 5 kilometers to miles -> ~3.106856
        (2, 'mi'),            # 2 miles to kilometers -> ~3.21869
        ('invalid', 'm'),     # Invalid input type for distance
        (-10, 'km'),         # Negative value handling
        (float('nan'), 'm'), # NaN input handling
    ]

    results = []
    
    for i in range(len(test_cases)):
        dist_val, target_unit = test_cases[i]
        
        try:
            result = convert_distance(dist_val, target_unit)
            
            if isinstance(result, float):
                formatted_result = f"{result:.6f}"
            else:
                formatted_result = str(result)
                
            results.append(f"Test {i+1}: Input ({dist_val}, '{target_unit}') -> Output: {formatted_result}")
        except Exception as e:
            # Catch any unexpected errors during conversion process
            error_msg = f"{e}" if isinstance(e, ZeroDivisionError) else "Unexpected Error"
            results.append(f"Test {i+1}: Input ({dist_val}, '{target_unit}') -> Output: ERROR - {error_msg}")

    print("\n".join(results))