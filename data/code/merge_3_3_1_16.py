def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.

    Args:
        temperatures (list[float]): A list of float values representing temperature readings.

    Returns:
        float: The average temperature as a float, or None if the input is empty.
    """
    return sum(temperatures) / len(temperatures)

if __name__ == '__main__':
    sample_readings = [23.5, 24.1, 22.8, 25.0, 23.9]
    
    average_temp = calculate_average_temperature(sample_readings)

    if average_temp is not None:
        print(f"The average temperature is {average_temp:.2f} degrees.")
    else:
        print("No data provided to calculate the average.")