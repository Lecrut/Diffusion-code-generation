def compare_temperatures(t1: float, t2: float) -> str:
    """
    Yields a comparison result string between two temperature values.
    
    Args:
        t1 (float): First temperature value.
        t2 (float): Second temperature value.
        
    Yields:
        str: A formatted string describing the difference and direction of temperatures.
    """
    diff = round(t1 - t2, 2)
    
    if abs(diff) < 0.01:
        yield f"T1 is equal to T2 (both at {t1:.2f} degrees)"
    elif diff > 0:
        yield f"T1 is warmer by {diff:+.2f} degrees compared to T2"
    else:
        yield f"T1 is colder by {-diff:.2f} degrees compared to T2"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    temp_a = 75.0
    temp_b = 68.5
    
    print("Comparing temperatures:")
    
    with compare_temperatures(temp_a, temp_b) as result:
        for message in result:
            print(message)