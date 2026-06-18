def convert_length(length: float, unit: str) -> float:
    """
    Converts a length value from meters to feet or vice versa.

    Args:
        length (float): The numerical value of the length.
        unit (str): The source unit ('m' for meters or 'ft' for feet).

    Returns:
        float: The converted length in feet if input was in meters, 
               otherwise returns the original length in meters.
    
    Note: This function assumes a direct conversion is needed based on the provided unit.
           If 'm', it converts to feet (1 meter = 3.28084 feet).
           If 'ft', it converts to meters (1 foot = 0.3048 meters) and returns in meters,
           as per standard conversion practice unless specified otherwise. 
           However, based on typical utility functions, let's return the value in the target unit opposite to input for clarity:
           Actually, re-reading the prompt "converts a length", usually implies converting FROM one TO another.
           Let's define it such that if 'm' is given, we convert TO feet. If 'ft' is given, we convert TO meters.
    """
    conversion_factors = {
        'm': 3.28084,      # Meters to Feet factor (1 m = 3.28084 ft)
        'ft': 0.3048       # Feet to Meters factor (1 ft = 0.3048 m)
    }

    if unit not in conversion_factors:
        raise ValueError(f"Unsupported unit '{unit}'. Supported units are 'm' and 'ft'.")

    return length * conversion_factors[unit]

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    sample_cases = [
        (1.0, 'm'),   # 1 meter to feet
        (25.4, 'ft'), # 25.4 feet to meters
        (1609.34, 'm',), # Approx distance of a mile in meters to miles? No, let's stick simple: 1 km approx is too complex without factor. Let's do standard conversions.
    ]

    for length_val, unit_str in sample_cases:
        result = convert_length(length_val, unit_str)
        print(f"Converted {length_val} {unit_str}: {result}")