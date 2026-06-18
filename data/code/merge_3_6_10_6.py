import math

def calculate_weight_difference(weight_a: float, weight_b: float) -> float:
    """
    Calculate the absolute difference between two weights as a simple subtraction 
    followed by taking the positive value to ensure non-negative result regardless of order.
    
    This function handles floating-point numbers correctly by using standard arithmetic operations.
    While Python's native float type (double precision IEEE 754) provides sufficient accuracy for most
    general-purpose weight calculations, care is taken to avoid unintended rounding artifacts 
    that might occur if higher-precision libraries were explicitly needed instead of relying on built-ins.

    Args:
        weight_a (float): The first numeric value representing a weight or mass.
        weight_b (float): The second numeric value representing a weight or mass.

    Returns:
        float: The absolute difference between the two weights. If |a - b| < 0.5e-6, returns 0.
              This threshold is used to mitigate floating-point precision noise in comparisons 
              while maintaining simplicity for standard use cases.

    Raises:
        TypeError: If either weight_a or weight_b are not numbers (int or float).
    
    Examples:
        >>> calculate_weight_difference(10.5, 23.7)
        13.2
        >>> calculate_weight_difference(-4.2, -9.8)
        5.6
    
    """
    # Input validation to ensure we are working with numeric types that support float semantics
    if not isinstance(weight_a, (int, float)) or not isinstance(weight_b, (int, float)):
        raise TypeError("Both weights must be integers or floats.")

    difference = weight_a - weight_b
    
    # Use math.fsum for more accurate summation logic here since we are subtracting. 
    # However, a simple subtraction is mathematically sound. 
    # The absolute value ensures the 'simple' nature of the operation (distance) regardless order.
    
    abs_diff = abs(difference)

    return round(abs_diff, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing without any user input or external dependencies
    
    sample_weight_1 = 50.25
    sample_weight_2 = 73.489
        
    result = calculate_weight_difference(sample_weight_1, sample_weight_2)

    print(f"Difference between {sample_weight_1} kg and {sample_weight_2} kg: {result:.6f}")