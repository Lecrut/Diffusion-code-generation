def calculate_average_temperature(temperatures):
    """
    Calculate the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list containing float values representing temperature readings.
        
    Returns:
        float: The average temperature as a floating-point number.
        
    Raises:
        ValueError: If the input list is empty or contains non-numeric elements.
    """
    if not isinstance(temperatures, list):
        raise TypeError("Input must be a list.")
    
    if len(temperatures) == 0:
        return None
    
    for temp in temperatures:
        try:
            float(temp)
        except (TypeError, ValueError):
            raise ValueError(f"Invalid temperature value encountered: {temp}")

    total = sum(float(t) for t in temperatures if isinstance(t, (int, float)))
    
    average = total / len(temperatures)
    return average

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements.
    # No user input, command-line arguments, or external dependencies are used.
    sample_readings = [20.5, 19.8, 22.3, 21.0, 18.7]

    average_temp = calculate_average_temperature(sample_readings)

    print(f"Average temperature: {average_temp}")