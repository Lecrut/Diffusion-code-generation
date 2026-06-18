def celsius_to_fahrenheit(temperature_dict: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        temperature_dict (dict): A dictionary where keys are location names 
                                and values are temperatures in degrees Celsius.
                                
    Returns:
        dict: A new dictionary with the same keys but values converted to 
              degrees Fahrenheit. Formula used: F = C * 9/5 + 32
    
    Raises:
        TypeError: If any value in the input dictionary is not a number (int or float).
    """
    fahrenheit_dict = {}
    
    for location, celsius_temp in temperature_dict.items():
        if not isinstance(celsius_temp, (int, float)):
            raise TypeError(f"Temperature reading for '{location}' must be numeric.")
        
        # Convert Celsius to Fahrenheit: F = C * 1.8 + 32
        fahrenheit_temp = celsius_temp * 9 / 5 + 32
        
        fahrenheit_dict[location] = round(fahrenheit_temp, 2)
    
    return fahrenheit_dict

if __name__ == '__main__':
    # Hard-coded sample temperature readings in Celsius
    sample_readings = {
        "New York": 20.5,
        "London": -3.75,
        "Tokyo": 18.0,
        "Sydney": 24.6,
        "Moscow": -8.2
    }

    # Perform the conversion and print results
    converted_readings = celsius_to_fahrenheit(sample_readings)
    
    for location, temp in converted_readings.items():
        print(f"{location}: {temp}°F")