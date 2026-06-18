def calculate_weight_difference(weight1: float, weight2: float) -> float:
    """
    Calculates the simple difference between two weights (absolute value).
    
    This function computes |weight1 - weight2| to ensure a non-negative 
    representation of the magnitude difference. It handles floating-point 
    numbers by using standard arithmetic operations which Python manages accurately enough for general use cases.

    Args:
        weight1 (float): The first weight value.
        weight2 (float): The second weight value.

    Returns:
        float: The absolute difference between the two weights.
    
    Examples:
        >>> calculate_weight_difference(10.5, 4.3)
        6.2
    
    Note:
        This implementation does not use external libraries and relies on Python's built-in 
        floating-point capabilities (IEEE 754). For extremely high precision requirements 
        in scientific contexts, the `decimal` module might be preferred over standard floats, 
        but this function adheres to the requirement of using general-purpose weights.
    """
    return abs(weight1 - weight2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_weight_1 = 450.75
    
    # Using different unit representations to test conversion logic if desired, 
    # but here we stick strictly to the task of calculating simple difference.
    sample_weight_2 = 389.2

    result = calculate_weight_difference(sample_weight_1, sample_weight_2)
    
    print(f"Difference between {sample_weight_1} and {sample_weight_2}:")
    print(result)