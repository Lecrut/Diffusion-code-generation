"""
Module to normalize arbitrary distance measurements into meters.

This module provides a function to convert any given distance value 
and its associated unit string (e.g., 'km', 'miles') directly into 
a standardized meter measurement using precise scaling factors.
"""

def normalize_to_meters(value: float, unit_str: str) -> float:
    """
    Convert a distance value and its unit to meters.

    Args:
        value (float): The numerical magnitude of the distance.
        unit_str (str): String representation of the unit (e.g., 'km', 'ft').

    Returns:
        float: Distance in meters, rounded to 6 decimal places for consistency.
    
    Raises:
        ValueError: If an unsupported or invalid unit is provided.
    """
    # Define scaling factors relative to meters
    scale_factors = {
        "m": 1.0,
        "mm": 0.001,
        "cm": 0.01,
        "km": 1000.0,
        "mi": 1609.344,
        "yd": 0.9144,
        "ft": 0.3048,
        "in": 0.0254,
    }

    # Normalize input unit string to lowercase for case-insensitive matching
    normalized_unit = unit_str.lower().strip()

    if normalized_unit not in scale_factors:
        raise ValueError(f"Unsupported or invalid distance unit '{unit_str}'. Supported units are {list(scale_factors.keys())}.")

    factor = scale_factors[normalized_unit]
    
    # Calculate result and round to avoid floating-point precision noise
    return round(value * factor, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        ("10", "km"),           # Expected: 10000.0 m
        (5000, ""),             # Default unit assumed 'm' if empty string passed as magnitude? 
                                # Correction based on task logic: Input must be value + unit. Let's adjust sample to valid inputs.
                                # Re-evaluating test cases for robustness and correctness.
    ]

    # Corrected Test Cases with explicit units
    samples = [
        (10, "km"),             # 10 km -> 10000 m
        (5, "miles"),           # 5 mi -> ~8046.72 m
        (3, "ft"),              # 3 ft -> 0.9144 m
        (100, "cm"),            # 100 cm -> 1.0 m
        (-5, "miles"),          # Negative distance handling: -8046.72 m
    ]

    print("Distance Normalization to Meters:")
    for val_str, unit in samples:
        try:
            value = float(val_str) if isinstance(val_str, str) else val_str
            result_meters = normalize_to_meters(value, unit)
            # Format output nicely showing original input and converted meters
            print(f"Input: {val_str} ({unit}) -> Output: {result_meters} m")
        except ValueError as e:
            print(f"Error processing sample '{val_str}' with unit '{unit}': {e}")

    # Additional edge case demonstration inside the block to ensure module utility is clear
    try:
        invalid_result = normalize_to_meters(10, "galaxy")
    except ValueError as e:
        print(f"Correctly caught error for unsupported unit 'galaxy': {e}")