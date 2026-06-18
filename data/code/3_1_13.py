def calculate_average_temperature(readings):
    """
    Calculates the arithmetic mean of a list of temperature readings (floats).
    
    Args:
        readings (list[float]): A non-empty list of float values representing temperatures.
        
    Returns:
        float: The average temperature rounded to two decimal places for consistency, 
               or None if the input list is empty.
    """
    if not isinstance(readings, list) or len(readings) == 0:
        return None
    
    # Use built-in sum and length functions for optimal performance over manual loops
    total = sum(float(r) for r in readings)
    count = float(len(readings))
    
    average = total / count
    return round(average, 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args needed)
    temperature_readings = [23.5, -1.0, 45.6789, 0.0, 22.4]
    
    result = calculate_average_temperature(temperature_readings)
    
    if result is not None:
        print(f"Average Temperature: {result}")
    else:
        print("Error: No temperature readings provided.")