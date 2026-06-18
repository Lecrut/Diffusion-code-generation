def absolute_temperature_difference(temp_a: float, temp_b: float) -> float:
    """
    Calculates the absolute difference between two temperatures.
    
    Args:
        temp_a (float): The first temperature value.
        temp_b (float): The second temperature value.
        
    Returns:
        float: The positive difference between the two temperatures.
    """
    return abs(temp_a - temp_b)

if __name__ == '__main__':
    # Sample values for testing without user input or network access
    sample_temp_1 = 25.0
    sample_temp_2 = -3.7
    
    result = absolute_temperature_difference(sample_temp_1, sample_temp_2)
    
    print(f"Difference between {sample_temp_1} and {sample_temp_2}: {result}")