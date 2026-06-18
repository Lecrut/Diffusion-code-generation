def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list of float values representing temperature readings.
        
    Returns:
        float: The average temperature rounded to two decimal places.
        
    Raises:
        ValueError: If the input list is empty.
    """
    if not temperatures:
        raise ValueError("The list of temperature readings cannot be empty.")

    return round(sum(temperatures) / len(temperatures), 2)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    sample_readings = [72.5, 68.3, 70.1, 74.9, 71.2]

    try:
        avg_temp = calculate_average_temperature(sample_readings)
        print(f"The average temperature is {avg_temp} degrees.")
    except ValueError as e:
        print(f"Error: {e}")