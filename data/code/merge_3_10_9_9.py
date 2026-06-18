import math

def temperatures_within_tolerance(val1: float, val2: float) -> bool:
    """
    Compare two temperature values to determine if their difference 
    is within a tolerance of 1 degree (absolute value).

    Args:
        val1: First temperature value.
        val2: Second temperature value.

    Returns:
        True if abs(val1 - val2) <= 1, otherwise False.
    """
    diff = math.fabs(val1 - val2)
    return diff <= 1

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or network access
    temp_a: float = 23.5
    temp_b: float = 24.8

    result = temperatures_within_tolerance(temp_a, temp_b)

    print(f"Difference between {temp_a} and {temp_b}:")
    print(f"Is within tolerance of 1 degree? {result}")