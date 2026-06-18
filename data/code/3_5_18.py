import sys

def filter_temperatures(temperatures):
    """
    Filters out temperature readings below 0°C from a list of temperatures.
    
    Args:
        temperatures (list[float]): List of floating-point numbers representing 
                                   the temperature in degrees Celsius.
        
    Returns:
        list[float]: A new list containing only the non-negative temperatures.
    """
    return [temp for temp in temperatures if temp >= 0]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or args)
    raw_readings = [-5, -2.5, 1, 3.7, 89.9, 40.2, -1, 0]
    
    filtered_result = filter_temperatures(raw_readings)
    
    print("Original readings:", raw_readings)
    print("Filtered temperatures (>= 0°C):", filtered_result)