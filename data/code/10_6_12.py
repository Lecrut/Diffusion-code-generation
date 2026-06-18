def compare_temperatures(t1: float, t2: float) -> str:
    """
    Generator function that yields a comparison result string between two temperatures.
    
    Args:
        t1 (float): First temperature value in degrees Celsius or Fahrenheit.
        t2 (float): Second temperature value in the same unit as t1.
        
    Yields:
        str: A formatted message indicating which temperature is higher and by how much.
             Example: 'T1 is warmer by 5.0 degrees' or 'T2 is warmer by 3.2 degrees'.
    
    Raises:
        ValueError: If both temperatures are identical (difference is zero).
    """
    difference = t1 - t2
    
    if abs(difference) < 1e-9:  # Treat near-zero differences as equal to avoid division issues or ambiguous output
        yield f"Both temperatures are the same."
    elif difference > 0:
        yield f"T1 is warmer by {difference:.1f} degrees."
    else:
        diff_abs = abs(difference)
        yield f"T2 is warmer by {diff_abs:.1f} degrees."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: T1 (30°C) vs T2 (25°C) -> T1 should be warmer
    print("Sample 1:")
    result_gen = compare_temperatures(30.0, 25.0)
    
    for message in result_gen:
        print(message)

    # Sample 2: T1 (-5°F) vs T2 (0°F) -> T2 should be warmer
    print("\nSample 2:")
    result_gen = compare_temperatures(-5.0, 0.0)
    
    for message in result_gen:
        print(message)

    # Sample 3: Identical temperatures
    print("\nSample 3:")
    result_gen = compare_temperatures(100.0, 100.0)
    
    for message in result_gen:
        print(message)