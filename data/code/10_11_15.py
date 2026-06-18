def compare_temperatures(temp_a: float | int, temp_b: float | int) -> str:
    """
    Compares two temperature values and returns a descriptive string.
    
    Parameters:
        temp_a (float or int): First temperature value.
        temp_b (float or int): Second temperature value.
        
    Returns:
        str: A description of the relationship between the two temperatures.
    """
    # Direct comparison is efficient in Python for built-in numeric types
    if temp_a > temp_b:
        return f"{temp_a} degrees is higher than {temp_b}."
    elif temp_a < temp_b:
        return f"{temp_a} degrees is lower than {temp_b}."
    else:
        return f"{temp_a} degrees and {temp_b} are equal."

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or files
    temp_1 = 25.5
    temp_2 = 30
    
    result = compare_temperatures(temp_1, temp_2)
    
    print("Comparison Result:")
    print(result)