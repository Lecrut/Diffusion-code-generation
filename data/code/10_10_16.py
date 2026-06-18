# Temperature Mean Calculator Module
def calculate_mean(temp1: float, temp2: float) -> str:
    """
    Calculates the arithmetic mean of two temperature readings.
    
    Args:
        temp1 (float): The first temperature reading.
        temp2 (float): The second temperature reading.
        
    Returns:
        str: The calculated mean formatted to two decimal places.
    """
    average = (temp1 + temp2) / 2
    return f"{average:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    reading_a = 23.5
    reading_b = 24.7
    
    result = calculate_mean(reading_a, reading_b)
    
    print(result)