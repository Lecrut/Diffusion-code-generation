def compare_temperatures(t1: float, t2: float) -> str:
    """
    Generator function that yields a comparison result string between two temperatures.
    
    Args:
        t1 (float): First temperature value in degrees Celsius or Fahrenheit.
        t2 (float): Second temperature value in the same unit as t1.
        
    Yields:
        str: A message describing how the first temperature compares to the second, 
             e.g., "T1 is warmer by 5 degrees" or "T2 is colder by 3 degrees".
             
    Note: This function does not require any external input or network access.
    """
    difference = t1 - t2
    
    if difference > 0:
        yield f"T1 is warmer by {difference} degrees."
    elif difference < 0:
        # Calculate the magnitude for T2's perspective (positive value)
        abs_diff = -difference
        yield f"T2 is colder by {abs_diff} degrees."
    else:
        yield "T1 and T2 are equal in temperature."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or command-line arguments.
    
    # Sample 1: T1 warmer than T2
    result_1 = compare_temperatures(30, 25)
    print("Sample 1 (T1=30, T2=25):")
    for msg in result_1:
        print(msg)

    # Sample 2: T2 colder than T1 (same as above logic but phrased differently by generator output)
    result_2 = compare_temperatures(7.5, -4.0)
    print("\nSample 2 (T1=7.5, T2=-4.0):")
    for msg in result_2:
        print(msg)

    # Sample 3: Equal temperatures
    result_3 = compare_temperatures(22, 22)
    print("\nSample 3 (T1=22, T2=22):")
    for msg in result_3:
        print(msg)