def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a given length from one metric/imperial unit to meters.

    Supported units (case-insensitive): 'm', 'km' (kilometers), 
    'cm' (centimeters), 'mm' (millimeters), 'ft' (feet), 'in' (inches).
    
    Args:
        length (float): The numerical value of the length.
        unit_type (str): The source unit as a string ('m', 'km', 'cm', 
                         'mm', 'ft', or 'in').

    Returns:
        float: The converted length in meters.

    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    
    # Conversion factors to meters (1 unit = X meters)
    conversion_factors = {
        'm': 1,
        'km': 1000,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254,
    }

    # Normalize input to lowercase for case-insensitive comparison
    unit_lower = unit_type.lower()

    if unit_lower not in conversion_factors:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Supported units are "
                        f"'m', 'km', 'cm', 'mm', 'ft', 'in'.")

    return length * conversion_factors[unit_lower]

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    
    test_cases = [
        (10, 'm'),           # 10 meters -> 10.0 m
        (5, 'km'),           # 5 kilometers -> 5000.0 m
        (200, 'cm'),         # 200 centimeters -> 2.0 m
        (30, 'mm'),          # 30 millimeters -> 0.03 m
        (10, 'ft'),          # 10 feet -> ~3.048 m
        (60, 'in'),          # 60 inches -> ~1.524 m
    ]

    for length_val, unit_str in test_cases:
        result = convert_length(length_val, unit_str)
        print(f"{length_val} {unit_str} is equal to {result:.4f} meters.")