def celsius_to_fahrenheit(celsius_dict: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celsius_dict (dict): A dictionary where keys are locations and values 
                            are temperatures in degrees Celsius as floats or ints.
        
    Returns:
        dict: A new dictionary with the same keys but values converted to 
              degrees Fahrenheit. Formula used: F = C * 9/5 + 32
        
    Raises:
        TypeError: If any value in the input dictionary is not a number (int or float).
    """
    fahrenheit_dict = {}
    
    for location, celsius_temp in celsius_dict.items():
        if isinstance(celsius_temp, (int, float)) and not isinstance(celsius_temp, bool):
            # Apply conversion formula: F = C * 1.8 + 32
            fahrenheit_temp = celsius_temp * 9 / 5 + 32
            fahrenheit_dict[location] = round(fahrenheit_temp)
        else:
            raise TypeError(f"Invalid temperature value for location '{location}': {celsius_temp}. Expected a number.")
            
    return fahrenheit_dict

if __name__ == '__main__':
    # Hard-coded sample data representing temperatures in Celsius at different locations
    celsius_readings = {
        "New York": 25.0,
        "London": 18,
        "Tokyo": -3.5,
        "Sydney": 29.67,
        "Moscow": 4
    }

    # Convert the dictionary and display results
    fahrenheit_readings = celsius_to_fahrenheit(celsius_readings)
    
    print("Temperature Conversion Results (Celsius to Fahrenheit):")
    for location in sorted(fahrenheit_readings.keys()):
        print(f"{location}: {fahrenheit_readings[location]}°F")