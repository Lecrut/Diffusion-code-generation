def absolute_temperature_difference(temp_a: float, temp_b: float) -> float:
    """
    Calculate the absolute difference between two temperatures.
    
    Args:
        temp_a (float): The first temperature value.
        temp_b (float): The second temperature value.
        
    Returns:
        float: The positive difference between the two values.
    """
    return abs(temp_a - temp_b)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    t1 = 25.0
    t2 = 37.5
    
    result = absolute_temperature_difference(t1, t2)
    
    print(f"Temperature difference: {result}")