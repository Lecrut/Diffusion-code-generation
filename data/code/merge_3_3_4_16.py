def celsius_to_fahrenheit(celsiuses: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.

    Args:
        celsiuses (dict): A dictionary where keys are locations (strings or hashable) 
                          and values are temperatures in degrees Celsius (floats).

    Returns:
        dict: A new dictionary with the same keys but values converted to Fahrenheit.
              Formula used: F = C * 9/5 + 32
    """
    fahrenheit_dict = {}
    for location, celsius_temp in celsiuses.items():
        # Ensure value is treated as float before calculation
        fahrenheit_temp = round(celsius_temp * 9 / 5 + 32)
        fahrenheit_dict[location] = fahrenheit_temp
    
    return fahrenheit_dict

if __name__ == '__main__':
    sample_readings = {
        "New York": 20.5,
        "London": -1.2,
        "Tokyo": 8.7,
        "Sydney": 14.3,
        "Berlin": -6.9
    }

    converted_temps = celsius_to_fahrenheit(sample_readings)
    
    print("Temperature Conversion Results:")
    for location, temp in converted_temps.items():
        print(f"{location}: {temp}°F")