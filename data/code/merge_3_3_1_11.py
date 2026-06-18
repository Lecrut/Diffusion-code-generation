def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings (floats).
    
    Args:
        temperatures (list[float]): A list containing float values representing 
                                   individual temperature readings.
        
    Returns:
        float: The average temperature rounded to two decimal places for precision,
               or None if the input list is empty.
    """
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    # Hard-coded sample values representing daily temperatures in Celsius
    readings = [23.5, 19.8, 24.0, 21.2, 26.7]
    
    average_temp = calculate_average_temperature(readings)
    
    print(f"Average Temperature: {average_temp:.2f} °C")