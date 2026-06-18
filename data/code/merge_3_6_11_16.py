def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the absolute difference between two weight values efficiently.

    Args:
        weight1 (float): The first numerical value representing a measurement of weight or quantity in some unit.
        weight2 (float): The second numerical value representing another measurement of weight or quantity in the same unit.

    Returns:
        float: The absolute difference between `weight1` and `weight2`.
    
    Efficiency Note:
        - Uses the built-in `abs()` function which is implemented in C for performance.
        - No unnecessary type conversions are performed before calculation; inputs are used directly as floats, 
          ensuring precision appropriate for weight measurements.

    Examples:
        >>> calculate_weight_difference(10.5, 4.2)
        6.3
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    val_a = 78.9
    val_b = 0.5
    
    result = calculate_weight_difference(val_a, val_b)
    
    print(f"The absolute difference is: {result}")