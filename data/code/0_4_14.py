import math

def inches_to_centimeters(inches: float) -> float:
    """
    Converts a length given in inches to centimeters using the exact conversion factor.
    
    The standard conversion is 1 inch = 2.54 cm exactly, as defined by international agreement.
    This function performs simple multiplication without rounding intermediate steps 
    (since 2.54 has finite decimal representation and Python floats are IEEE 754 doubles).

    Args:
        inches (float): The length in inches. Must be a non-negative float or int.

    Returns:
        float: The equivalent length in centimeters.

    Raises:
        TypeError: If the input is not numeric.
    """
    if not isinstance(inches, (int, float)):
        raise TypeError("Input must be an integer or float representing inches.")
    
    return inches * 2.54

if __name__ == '__main__':
    # Sample test cases with hard-coded values as per requirements
    sample_inches = [1, 36, 72.0]
    
    for inch_value in sample_inches:
        cm_value = inches_to_centimeters(inch_value)
        print(f"{inch_value} inches is equal to {cm_value:.4f} centimeters")