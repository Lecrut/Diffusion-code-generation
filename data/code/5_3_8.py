def calculate_ratio(measurement1: float, measurement2: float) -> float:
    """
    Calculate the ratio of two positive length measurements.
    
    Args:
        measurement1 (float): The first length measurement.
        measurement2 (float): The second length measurement.
        
    Returns:
        float: The result of dividing measurement1 by measurement2.
        
    Raises:
        ValueError: If either input is not a positive number.
    """
    if not isinstance(measurement1, (int, float)) or not isinstance(measurement2, (int, float)):
        raise ValueError("Inputs must be numeric.")
    
    if measurement1 <= 0 or measurement2 <= 0:
        raise ValueError("Both measurements must be positive numbers.")
        
    return measurement1 / measurement2

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input.
    val_a = 10.5
    val_b = 4
    
    try:
        result = calculate_ratio(val_a, val_b)
        print(result)
    except ValueError as e:
        print(f"Error: {e}")