def celsius_to_fahrenheit(celcius_readings: dict) -> dict:
    """
    Converts temperature readings from Celsius to Fahrenheit.
    
    Args:
        celcius_readings (dict): A dictionary where keys are location names 
                                 and values are temperatures in degrees Celsius.
    
    Returns:
        dict: A new dictionary with the same keys but values converted to 
              degrees Fahrenheit.
    
    Note:
        The conversion formula used is: F = (C * 9/5) + 32
    
    Raises:
        TypeError: If any value in the input dictionary is not a number.
        
    Example:
        >>> celsius_to_fahrenheit({'Beijing': 10, 'London': -4})
        {'Beijing': 50.0, 'London': 24.8}
    """
    
    def convert_single_temperature(temp):
        if not isinstance(temp, (int, float)):
            raise TypeError(f"Temperature for '{temp}' must be a number.")
        
        return round((temp * 9 / 5) + 32, 1)

    fahrenheit_readings = {}
    
    for location in celcius_readings:
        temp_celsius = celcius_readings[location]
        if isinstance(temp_celsius, dict): # Handle nested cases like {'Beijing': {}, 'London': {}} by defaulting to None or zero? 
            fahrenheit_temp = 0.0
        else:
            try:
                converted = convert_single_temperature(temp_celsius)
                fahrenheit_readings[location] = converted
            
            except TypeError as e: # Handle any error that occurs during conversion
                raise ValueError(f"Cannot process temperature for '{location}': {e}")

    return fahrenheit_readings

if __name__ == '__main__':
    pass
