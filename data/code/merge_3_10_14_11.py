def temperature_difference(temp_a: float, temp_b: float) -> float:
    """
    Calculate the absolute difference between two temperatures.
    
    Args:
        temp_a (float): The first temperature value.
        temp_b (float): The second temperature value.
        
    Returns:
        float: The positive difference between the two temperatures.
    """
    return abs(temp_a - temp_b)

if __name__ == '__main__':
    # Hard-coded sample values for testing; no user input required.
    t1 = 20.5
    t2 = 37.9
    
    result = temperature_difference(t1, t2)
    
    print(f"Difference between {t1} and {t2}: {result}")