def calculate_average_temperature(readings):
    """
    Calculate the arithmetic mean of a list of temperature readings.

    Parameters:
        readings (list[float]): A list of float values representing temperatures.

    Returns:
        float: The average temperature if input is valid; None otherwise.
    """
    if not isinstance(readings, list) or len(readings) == 0:
        return None
    
    total = sum(float(x) for x in readings)
    return total / len(readings)

if __name__ == '__main__':
    # Sample data hard-coded as per requirements (no external files or input needed)
    sample_readings = [21.5, 23.0, 19.8, 24.2, 22.7]
    
    if calculate_average_temperature(sample_readings):
        print(f"Average temperature: {calculate_average_temperature(sample_readings)}")