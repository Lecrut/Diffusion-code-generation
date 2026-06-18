def compare_temperatures(t1: float, t2: float) -> str:
    """
    Generator function that yields a comparison result string between two temperatures.
    
    Args:
        t1 (float): First temperature value in degrees Celsius or Fahrenheit.
        t2 (float): Second temperature value in the same unit as t1.
        
    Yields:
        str: A descriptive message indicating which temperature is higher and by how much.
             Format examples: 'T1 is warmer by X.XX degrees', 'T2 is warmer by X.XX degrees'
    
    Examples:
        >>> list(compare_temperatures(30, 45))
        ['T2 is warmer by 15.00 degrees']
    """
    difference = t1 - t2
    
    if abs(difference) < float('inf') and not (difference == float('-inf') or difference == float('inf')):
        # Handle potential infinite values gracefully, though inputs are expected to be finite floats
        is_t1_warmer = difference > 0
        
        message_prefix = f"T1" if is_t1_warmer else "T2"
        magnitude = abs(difference)
        
        yield f"{message_prefix} is warmer by {magnitude:.2f} degrees"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample 1: T1 (30°C), T2 (45°C) -> T2 should be reported as warmer
    print("Sample 1:")
    result_1 = list(compare_temperatures(30, 45))
    for msg in result_1:
        print(msg)

    # Sample 2: T1 (-5°F), T2 (10°F) -> T2 should be reported as warmer
    print("\nSample 2:")
    result_2 = list(compare_temperatures(-5, 10))
    for msg in result_2:
        print(msg)

    # Sample 3: Equal temperatures
    print("\nSample 3 (Equal):")
    result_3 = list(compare_temperatures(25.5, 25.5))
    for msg in result_3:
        print(msg)

    # Sample 4: T1 is warmer by a small margin
    print("\nSample 4:")
    result_4 = list(compare_temperatures(70.8, 69.9))
    for msg in result_4:
        print(msg)