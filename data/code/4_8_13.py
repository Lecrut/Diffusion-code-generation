import math

def normalize_distance(value: float, unit: str) -> float:
    """
    Normalize a distance measurement to meters.
    
    Args:
        value (float): The numeric magnitude of the distance.
        unit (str): The string representation of the source unit.
        
    Returns:
        float: The equivalent distance in meters.
        
    Supported units: 'mm', 'cm', 'm', 'km', 'mi', 'ft', 'yd'
    
    Raises:
        ValueError: If an unsupported unit is provided or value is invalid.
    """
    if not isinstance(value, (int, float)) or math.isnan(float(value)):
        raise ValueError("Value must be a valid number.")
        
    supported_units = {
        'mm': 0.001,
        'cm': 0.01,
        'm': 1.0,
        'km': 1000.0,
        'mi': 1609.34721485, # International mile in meters
        'ft': 0.3048,
        'yd': 0.9144
    }
    
    unit = unit.lower().strip()
    
    if unit not in supported_units:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are {list(supported_units.keys())}.")
        
    return value * supported_units[unit]

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    test_cases = [
        ('50', 'mm'),
        ('1234.567', 'cm'),
        (8, 'm'),
        (0.9, 'km'),
        (3, 'mi'), # Approx 4828 meters
        (6, 'ft'),
        (2, 'yd')
    ]

    print("Distance Normalization to Meters")
    print("-" * 35)
    
    for value_str, unit in test_cases:
        try:
            numeric_value = float(value_str)
            meters = normalize_distance(numeric_value, unit)
            # Formatting output with reasonable precision based on input magnitude
            if abs(meters) < 1e-6 and not math.isclose(0.0, meters):
                print(f"{value_str} {unit:2s} -> ~{meters:.3f} m")
            else:
                print(f"{value_str} {unit:2s} -> {meters:.4f} m")
        except ValueError as ve:
            print(f"Error processing '{value_str}' with unit '{unit}': {ve}")

    # Demonstrate error handling for invalid units and values
    print("-" * 35)
    
    try:
        normalize_distance(-10, "invalid_unit")
    except ValueError as ve:
        print(f"\nCaught expected error for invalid unit: {ve}")
        
    try:
        # NaN handling simulation (though float('-nan') is technically valid input to the function logic)
        nan_val = float('nan') 
        normalize_distance(nan_val, "m")
    except ValueError as ve:
        print(f"\nCaught expected error for invalid numeric value: {ve}")

    # Demonstrate zero case
    result_zero = normalize_distance(0.0, 'km')
    print("-" * 35)
    print("Zero Distance Test:")
    print(f"{result_zero} m")