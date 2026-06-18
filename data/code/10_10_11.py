def calculate_temperature_mean(temp1: float, temp2: float) -> str:
    """
    Calculates the arithmetic mean of two temperature readings and returns it formatted to two decimal places.
    
    Args:
        temp1 (float): The first temperature reading.
        temp2 (float): The second temperature reading.
        
    Returns:
        str: The calculated average rounded to two decimal places as a string.
    """
    mean_value = (temp1 + temp2) / 2
    return f"{mean_value:.2f}"

if __name__ == '__main__':
    # Hard-coded sample values for testing, ensuring no user input or external dependencies are needed.
    reading_a: float = -4.50
    reading_b: float = 18.75
    
    result = calculate_temperature_mean(reading_a, reading_b)
    
    print(result)