import re

def is_positive_number(value: str) -> bool:
    """Check if a string represents a positive number."""
    try:
        num = float(value)
        return num > 0
    except ValueError:
        return False

def calculate_ratio(length1: float, length2: float) -> tuple[float, int]:
    """Calculate the ratio of two lengths and count decimal places.

    Args:
        length1 (float): First positive number representing a length.
        length2 (float): Second positive number representing a length.

    Returns:
        tuple: A tuple containing the calculated float division result 
               and an integer representation for cleaner formatting without trailing zeros.
    
    Raises:
        ValueError: If inputs are not both positive numbers.
    """
    if not is_positive_number(str(length1)) or not is_positive_number(str(length2)):
        raise ValueError("Both lengths must be valid positive numbers.")

    result = length1 / length2
    
    # Format the integer version to match significant digits of float for cleaner output
    int_rep = round(result)
    
    return result, int_rep

def format_output(float_val: float, int_val: int) -> str:
    """Format the ratio string with trailing zeros removed from non-integers."""
    if float_val == int_val:
        return f"{int_val:.0f}" + " : 1"
    
    # Find where to start removing decimal places (after last significant digit other than integer part)
    formatted_str = str(float_val).rstrip('0')[:-1] or '0'
    
    if '.' not in float_val:
        return f"{int_val:.0f} : 1"

if __name__ == '__main__':
    pass
