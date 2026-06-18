import math

def convert_length(value: float, unit_from: str) -> tuple[float, str]:
    """
    Converts a length value from one unit to another meters and returns 
    (value_in_meters, source_unit_str).
    
    Supported units in input: 'm', 'km', 'cm', 'mm', 'ft', 'in'.
    All conversions are normalized to base SI meter first.

    Args:
        value (float): The length value to convert.
        unit_from (str): The source unit ('m', 'km', 'cm', 'mm', 'ft', 'in').

    Returns:
        tuple[float, str]: A tuple containing the converted length in meters 
                           and the original input unit string for reference.
    
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    # Conversion factors to meters (1 unit = X meters)
    conversion_factors_to_meters = {
        'm': 1,
        'km': 1_000,
        'cm': 0.01,
        'mm': 0.001,
        'ft': 0.3048,
        'in': 0.0254
    }

    if unit_from not in conversion_factors_to_meters:
        raise ValueError(f"Unsupported unit '{unit_from}'. Supported units are {list(conversion_factors_to_meters.keys())}")

    meters = value * conversion_factors_to_meters[unit_from]
    
    return (meters, f"{value} {unit_from}" if isinstance(value, int) or type(value).__name__ != 'numpy.float64' else str(value))

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    samples = [
        ('5', 'm'),      # 5 meters -> (5.0 m)
        ('10 km', None), # Actually the input expects float for value based on type hint, 
                         # but let's assume user passed int/float as per typical usage of value: float in func def.
                         # Correction to align with function signature which takes numeric types explicitly?
                         # Re-reading task: "accepts a length and a unit type". Usually implies numbers for length.
                         # Let's use standard floats/integers for the first argument as per typical usage of convert_length(value, unit).
    ]

    # Adjusted sample list to strictly follow function signature (value=float/unit_from=str)
    test_cases = [
        {'val': 5.0, 'unit': 'm', 'expected_meters': 5.0},
        {'val': 1000, 'unit': 'km', 'expected_meters': 1_000_000.0},
        {'val': 254, 'unit': 'cm', 'expected_meters': 2.54},
        {'val': 3.281, 'unit': 'ft', 'expected_meters': 1.0}, # Approximate foot to meter conversion
    ]

    for case in test_cases:
        res = convert_length(case['val'], case['unit'])
        if abs(res[0] - case['expected_meters']) < 0.001:
            print(f"Test passed for {case['val']} {case['unit']}: Result is {res[0]} meters.")
        else:
            print(f"Test FAILED for {case['val']} {case['unit']}: Expected ~{case['expected_meters']}, got {res[0]}.")

    # Demonstration of error handling
    try:
        convert_length(1, 'yard')
    except ValueError as e:
        print(f"Caught expected error for unsupported unit 'yard': {e}")