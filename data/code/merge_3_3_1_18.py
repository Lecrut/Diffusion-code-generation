def calculate_average_temperature(temperatures: list[float]) -> float:
    """
    Calculate the arithmetic mean of a list of temperature readings.
    
    Uses sum() which is implemented in C for efficiency, and returns the result divided by count.
    
    Args:
        temperatures (list[float]): A non-empty list of float values representing temperature readings.
        
    Returns:
        float: The average temperature rounded to 4 decimal places for consistency.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("The list of temperature readings cannot be empty.")
    
    return round(sum(temperatures) / len(temperatures), 4)

if __name__ == '__main__':
    # Hard-coded sample values for testing, no user input required.
    sample_readings = [20.5, 19.8, 21.3, 20.9, 22.1]
    
    average_temp = calculate_average_temperature(sample_readings)
    print(f"The average temperature is: {average_temp}°C")