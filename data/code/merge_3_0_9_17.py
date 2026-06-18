import math

# Supported units: 'm', 'km', 'cm', 'mm' (metric)
UNIT_TO_METER = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
}

def convert_length(value: float, source_unit: str, target_unit: str) -> float:
    """
    Convert a length value from one metric unit to another.
    
    Args:
        value (float): The numerical value of the length.
        source_unit (str): Source unit ('m', 'km', 'cm', 'mm').
        target_unit (str): Target unit ('m', 'km', 'cm', 'mm').
        
    Returns:
        float: Converted length in the target unit.
        
    Raises:
        ValueError: If units are not supported or value is invalid.
    """
    if source_unit not in UNIT_TO_METER or target_unit not in UNIT_TO_METER:
        raise ValueError(f"Unsupported units: {source_unit}, {target_unit}")
    
    # Convert to meters first, then to the target unit
    meters = value * UNIT_TO_METER[source_unit]
    result_meters = meters / UNIT_TO_METER[target_unit]
    
    return round(result_meters, 6)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test case 1: km to m
    length_km_to_m = convert_length(2.5, 'km', 'm')
    print(f"2.5 km in meters is {length_km_to_m} m")

    # Test case 2: cm to mm
    length_cm_to_mm = convert_length(100, 'cm', 'mm')
    print(f"100 cm in millimeters is {length_cm_to_mm} mm")

    # Test case 3: mm to km (small value)
    length_mm_to_km = convert_length(5000, 'mm', 'km')
    print(f"5000 mm in kilometers is {length_mm_to_km} km")

    # Test case 4: m to cm
    length_m_to_cm = convert_length(1.234, 'm', 'cm')
    print(f"1.234 meters in centimeters is {length_m_to_cm} cm")