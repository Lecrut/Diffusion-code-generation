import time

def filter_temperatures(readings: list[float]) -> list[float]:
    """
    Filters out temperature readings below freezing (0°C) from a given list.
    
    Args:
        readings (list[float]): A list of floating-point numbers representing temperatures in Celsius.
        
    Returns:
        list[float]: A new list containing only the non-negative temperature values.
    """
    return [reading for reading in readings if reading >= 0]

if __name__ == '__main__':
    # Hard-coded sample data without user input, CLI args, or network access
    raw_readings = [-5.2, -1.8, 0.0, 3.4, 7.6, 9.1, -0.5]

    filtered_temperatures = filter_temperatures(raw_readings)
    
    print(f"Original readings: {raw_readings}")
    print(f"Filtered temperatures (>= 0°C): {filtered_temperatures}")