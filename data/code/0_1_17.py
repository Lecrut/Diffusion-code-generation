def convert_length(length: float, unit_type: str) -> float:
    """
    Converts a given length from one imperial/US customary unit to meters.
    
    Supported units (input): 'm', 'ft', 'in'
    Output is always in meters ('m').

    Args:
        length: The numerical value of the length.
        unit_type: String representing the input unit ('m', 'ft', or 'in').

    Returns:
        float: Equivalent length in meters.
    
    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    conversion_factors = {
        'm': 1.0,
        'ft': 0.3048,
        'in': 0.0254,
    }

    if unit_type not in conversion_factors:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Supported units are m, ft, in.")

    return length * conversion_factors[unit_type]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_tests = [
        (5.0, 'm'),      # 5 meters -> 5.0
        (10.0, 'ft'),    # 10 feet -> ~3.048
        (24.0, 'in'),    # 24 inches -> 0.6096
    ]

    for length_val, unit_str in sample_tests:
        result = convert_length(length_val, unit_str)
        print(f"{length_val} {unit_str.upper()} is equal to {result:.5f} m")