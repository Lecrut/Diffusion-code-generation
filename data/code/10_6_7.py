def compare_temperatures(t1: float, t2: float) -> str:
    """
    Yields a string describing the comparison between two temperature values.
    
    Args:
        t1 (float): First temperature value in degrees Celsius or Fahrenheit.
        t2 (float): Second temperature value in degrees Celsius or Fahrenheit.
        
    Yields:
        A descriptive string indicating which temperature is higher and by how much.
    """
    difference = abs(t1 - t2)
    
    if t1 > t2:
        yield f"T1 is warmer than T2 by {difference:.2f} degrees."
    elif t2 > t1:
        yield f"T2 is warmer than T1 by {difference:.2f} degrees."
    else:
        yield "T1 and T2 are the same temperature."

if __name__ == '__main__':
    # Hard-coded sample values for testing
    temp_a = 25.0
    temp_b = 30.5
    
    print("--- Temperature Comparison Results ---")
    
    result_messages = list(compare_temperatures(temp_a, temp_b))
    
    for message in result_messages:
        print(message)