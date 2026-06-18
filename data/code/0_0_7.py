"""
Script to convert a given length from meters to feet.

This module provides a function to perform the conversion using the standard factor,
where 1 meter equals approximately 3.28084 feet.
"""

def meters_to_feet(meters: float) -> float:
    """
    Converts a distance measured in meters to its equivalent in feet.

    The conversion uses the constant defined by international agreement:
        1 meter = 3.280839895013123... feet

    Args:
        meters (float): The length value in meters. Must be non-negative for physical sense, 
                       though the math holds for any float input.

    Returns:
        float: The equivalent length in feet.

    Examples:
        >>> meters_to_feet(1)
        3.28084
        >>> round(meters_to_feet(5), 4)
        16.4042
    """
    FEET_PER_METER = 3.280839895
    return meters * FEET_PER_METER

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    # No interactive input is used in this block.

    # Sample cases to demonstrate functionality and include output
    test_values = [1, 2.5, 10, -5]

    for meter_value in test_values:
        feet_value = meters_to_feet(meter_value)
        print(f"{meter_value} meters is equal to {feet_value:.4f} feet")