def convert_temp(celsius_list: list) -> list:
    """
    Converts a list of temperature readings from Celsius to Fahrenheit.
    
    The conversion formula is F = C * 9/5 + 32.
    This implementation uses a list comprehension for efficiency and readability.

    Args:
        celsius_list (list): A list of floating-point or integer values representing temperatures in Celsius.

    Returns:
        list: A new list containing the corresponding temperature values in Fahrenheit.
    
    Example:
        >>> convert_temp([0, 25])
        [32.0, 77.0]
    """
    return [c * (9 / 5) + 32 for c in celsius_list]

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_celsius = [-40, -10, 0, 25.5, 100]
    
    converted_fahrenheit = convert_temp(sample_celsius)
    
    print("Celsius:", sample_celsius)
    print("Fahrenheit:", converted_fahrenheit)