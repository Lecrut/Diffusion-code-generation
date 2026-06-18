def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list of float values representing temperature readings.
        
    Returns:
        float: The average temperature rounded to two decimal places for consistency, 
               or None if the input is empty.
    """
    if not temperatures:
        return None
    
    # Using sum() and len() which are optimized C implementations in Python's standard library
    total = sum(temperatures)
    count = len(temperatures)
    
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_readings = [23.5, -4.1, 18.0, 29.7, 12.3]
    
    result = calculate_average_temperature(sample_readings)
    
    if result is not None:
        print(f"The average temperature of the readings {sample_readings} is {result}.")
    else:
        print("No data provided to calculate an average.")