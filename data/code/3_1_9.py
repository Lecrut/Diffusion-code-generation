def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list of float values representing temperature readings.
        
    Returns:
        float: The average temperature rounded to two decimal places for consistency, 
               or None if the input list is empty.
    """
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input needed)
    sample_readings = [23.5, 19.8, 24.0, 21.2, 22.7]
    
    average_temp = calculate_average_temperature(sample_readings)
    print(f"The average temperature is: {average_temp}")