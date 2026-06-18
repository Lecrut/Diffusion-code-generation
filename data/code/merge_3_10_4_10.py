import statistics

def find_extremes(temperatures):
    """
    Finds the maximum and minimum temperatures in a list efficiently.
    
    Args:
        temperatures (list[float]): A list of temperature readings.
        
    Returns:
        tuple[float, float]: A tuple containing (min_temp, max_temp).
        
    Raises:
        ValueError: If the input list is empty or None.
    """
    if not isinstance(temperatures, list) or len(temperatures) == 0:
        raise ValueError("Input must be a non-empty list of numbers.")
    
    # Using min() and max() built-ins are implemented in C for efficiency (CPython).
    return (min(temperatures), max(temperatures))

if __name__ == '__main__':
    sample_readings = [23.5, 19.0, 27.8, 24.2, 18.5]
    
    min_temp, max_temp = find_extremes(sample_readings)
    
    print(f"Minimum Temperature: {min_temp}")
    print(f"Maximum Temperature: {max_temp}")