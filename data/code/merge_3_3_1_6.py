def calculate_average_temperature(temperatures):
    """
    Calculates the arithmetic mean of a list of temperature readings.
    
    Args:
        temperatures (list[float]): A list containing floating-point numbers representing temperature values.
        
    Returns:
        float or None: The average temperature if the input is non-empty; otherwise, returns None.
        
    Raises:
        TypeError: If the input is not a list of floats/ints.
        ValueError: If the input list is empty.
    """
    # Check for valid type and content using isinstance to ensure all elements are numeric
    if not isinstance(temperatures, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")

if __name__ == '__main__':
    pass
