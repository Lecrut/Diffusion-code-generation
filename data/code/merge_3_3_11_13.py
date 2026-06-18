def convert_temp(celsius_list):
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is: F = (C * 9/5) + 32
    
    Args:
        celsius_list (list[float]): A list containing temperature values in degrees Celsius.
        
    Returns:
        list[float]: A new list with the corresponding temperatures converted to Fahrenheit.
    
    Example:
        >>> convert_temp([0, 10, 25])
        [32.0, 50.0, 77.0]
    """
    return [(c * 9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_celsius = [0, 10.5, -4, 100]
    
    result_fahrenheit = convert_temp(sample_celsius)
    
    print("Celsius:", sample_celsius)
    print("Fahrenheit:", result_fahrenheit)