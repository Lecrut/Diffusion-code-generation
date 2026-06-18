def calculate_mean(temp1: float, temp2: float) -> str:
    """
    Calculates the arithmetic mean of two temperature readings 
    and returns it formatted to two decimal places as a string.
    
    Args:
        temp1 (float): First temperature reading.
        temp2 (float): Second temperature reading.
        
    Returns:
        str: Formatted mean value rounded to two decimal places.
    """
    average = (temp1 + temp2) / 2
    return f"{average:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    reading_a = 23.5
    reading_b = 24.7
    
    result_mean = calculate_mean(reading_a, reading_b)
    print(result_mean)