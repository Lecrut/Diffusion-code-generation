def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings (floats).
    
    Args:
        temperatures (list[float]): A list containing numeric temperature values.
        
    Returns:
        float: The average temperature rounded to two decimal places, or None if input is empty.
    """
    if not temperatures:
        return None
    
    # Using sum() and len() for efficiency with built-in functions as requested
    total = sum(temperatures)
    count = len(temperatures)
    
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    # Hard-coded sample values representing temperature readings in Celsius
    sample_readings = [15.4, -3.7, 20.1, 8.9, 22.5]
    
    result = calculate_average_temperature(sample_readings)
    
    if result is not None:
        print(f"Average Temperature: {result}°C")
    else:
        print("Error: No temperature readings provided.")