import time

def compare_temperatures(temp_a: float | int, temp_b: float | int) -> str:
    """
    Compares two temperature values efficiently and returns a descriptive string.

    Args:
        temp_a (float|int): First temperature value.
        temp_b (float|int): Second temperature value.

    Returns:
        str: Description of the comparison result ('A is higher', 'B is higher', or 'Equal').
    """
    # Direct comparison without unnecessary object creation ensures efficiency for all numeric types in Python 3.x.
    if temp_a > temp_b:
        return f"Temperature A ({temp_a}) is higher than Temperature B ({temp_b})."
    elif temp_b > temp_a:
        return f"Temperature B ({temp_b}) is higher than Temperature A ({temp_a})."
    else:
        return "Temperatures are equal."

if __name__ == '__main__':
    # Hard-coded sample values for testing without external input or files.
    sample_values = [
        (25.0, 30.1),      # A is lower than B
        (72, 68),          # A is higher than B (integers)
        (-4.5, -4.5),     # Equal values
        (100, float('inf')), # Edge case with infinity if supported by runtime context
    ]

    for val_a, val_b in sample_values:
        result = compare_temperatures(val_a, val_b)
        print(result)