def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list of float values representing temperature readings.
        
    Returns:
        float: The average temperature rounded to two decimal places, or None if the input is empty.
    """
    if not temperatures:
        return None
    
    # Using sum() and len() for efficiency with built-in functions as requested
    total = sum(temperatures)
    count = len(temperatures)
    
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    # Hard-coded sample values to ensure the module runs without user input or external dependencies
    sample_readings = [23.5, -4.1, 18.9, 0.0, 27.3]
    
    result = calculate_average_temperature(sample_readings)
    
    if result is not None:
        print(f"The average temperature is {result} degrees.")
    else:
        print("No data provided to calculate the average.")