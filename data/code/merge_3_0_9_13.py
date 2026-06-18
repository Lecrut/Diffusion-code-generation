import math

# Supported units: 'm', 'cm', 'mm', 'km' (metric)
UNIT_TO_METER = {
    'm': 1,
    'cm': 0.01,
    'mm': 0.001,
    'km': 1000,
}

def convert_length(value: float, source_unit: str, target_unit: str) -> float:
    """
    Converts a length value from one metric unit to another.
    
    Args:
        value (float): The numerical value of the length.
        source_unit (str): The original unit ('m', 'cm', 'mm', 'km').
        target_unit (str): The desired unit ('m', 'cm', 'mm', 'km').
        
    Returns:
        float: The converted length in the target unit.
        
    Raises:
        ValueError: If an unsupported unit is provided.
    """
    if source_unit not in UNIT_TO_METER or target_unit not in UNIT_TO_METER:
        raise ValueError(f"Unsupported units: {source_unit}, {target_unit}. Supported: m, cm, mm, km")

    # Convert to meters first as a common base unit for calculation efficiency and cleanliness
    value_in_meters = value * UNIT_TO_METER[source_unit]
    
    # Then convert from meters to the target unit
    return value_in_meters / UNIT_TO_METER[target_unit]

if __name__ == '__main__':
    # Hard-coded sample values for testing
    
    test_cases = [
        (10, 'cm', 'm'),           # 10 cm -> 0.1 m
        (5000, 'mm', 'km'),       # 5000 mm -> 0.005 km
        (2, 'km', 'm'),           # 2 km -> 2000 m
        (3.5, 'm', 'cm'),         # 3.5 m -> 350 cm
    ]

    for val, src, tgt in test_cases:
        result = convert_length(val, src, tgt)
        print(f"{val} {src} is equal to {result:.6f} {tgt}")