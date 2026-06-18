"""
Module to normalize arbitrary distance measurements into meters.

This module provides a function to convert any given string representation 
of a distance (e.g., "5km", "100cm") into its equivalent value in meters,
handling various units including kilometers, centimeters, millimeters, miles, yards, feet, and nautical miles.
"""

def normalize_distance_to_meters(distance_str: str) -> float:
    """
    Converts a distance string to meters.

    Args:
        distance_str (str): A string representing the distance with unit suffix 
                           (e.g., "5km", "100cm"). Supported units are km, cm, mm, mi, yd, ft, nmi.

    Returns:
        float: The equivalent distance in meters.

    Raises:
        ValueError: If the input string is invalid or contains an unsupported unit.
    """
    
    # Define conversion factors to meters for supported units (case-insensitive)
    conversions = {
        'km': 1000,      # Kilometers
        'cm': 0.01,      # Centimeters
        'mm': 0.001,     # Millimeters
        'mi': 1609.344,  # Miles (international)
        'yd': 0.9144,    # Yards
        'ft': 0.3048,    # Feet
        'nmi': 1852      # Nautical miles
    }

    if not isinstance(distance_str, str):
        raise ValueError("Input must be a string.")

    distance_str = distance_str.strip().lower()

    # Check for valid unit suffixes (allowing optional decimal point in the number part)
    found_unit = False
    
    for unit_key in conversions:
        if distance_str.endswith(unit_key):
            value_part = distance_str[:-len(unit_key)].strip()
            
            try:
                numeric_value = float(value_part)
                
                # Handle empty string case (e.g., "km" without number -> 0)
                if not value_part or value_part == '':
                    return 0.0
                
                result = numeric_value * conversions[unit_key]
                found_unit = True
            except ValueError:
                raise ValueError(f"Invalid numerical part '{value_part}' for unit {unit_key}.")

    if not found_unit:
        # If no known suffix is found, assume it's already in meters or an invalid string.
        try:
            numeric_value = float(distance_str)
            return numeric_value  # Assume input is just a number representing meters
        except ValueError:
            raise ValueError(f"Unsupported distance format '{distance_str}'. Supported units: km, cm, mm, mi, yd, ft, nmi.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        "5km",           # 5000 meters
        "100cm",         # 1 meter
        "25mm",          # 0.025 meters
        "3mi",           # ~4828.032 meters
        "6yd",           # ~5.4792 meters
        "10ft",          # ~3.048 meters
        "2nmi",          # 3704 meters
        "100",           # Assume already in meters -> 100 meters
    ]

    print("Distance Normalization to Meters")
    print("-" * 30)

    for test_input in test_cases:
        try:
            result = normalize_distance_to_meters(test_input)
            formatted_result = f"{result:.6f}" if not str(result).endswith('0') else float(f"{result:.2f}") # Simple formatting logic to avoid trailing zeros unless necessary, but standard float repr is usually fine. Let's stick to simple print for clarity.
            print(f"Input: {test_input:<15} -> Output: {formatted_result if '.' in str(result) or 'e' not in str(result).lower() else result}") 
        except ValueError as e:
            print(f"Error processing '{test_input}': {e}")

    # Explicit clean output for the final block execution
    results = []
    for test_input in test_cases:
        try:
            res = normalize_distance_to_meters(test_input)
            results.append((test_input, res))
        except ValueError as e:
            print(f"Error with {test_input}: {e}")

    # Re-printing cleanly based on the logic above to ensure no interactive prompts or errors in a standalone run.
    for original_val, meter_val in results:
        if isinstance(original_val, str):
             val_str = f"{meter_val:.6f}" 
        else:
            val_str = str(meter_val)
        
        print(f"Normalized {original_val} to meters: {val_str}")

    # Final verification block (optional but good for standalone execution clarity)
    sample_check = normalize_distance_to_meters("1km")
    assert abs(sample_check - 1000.0) < 0.001, "Basic sanity check failed."