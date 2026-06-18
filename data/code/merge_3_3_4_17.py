def celsius_to_fahrenheit(temperature_dict: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        temperature_dict (dict): A dictionary where keys are location names 
                                and values are temperatures in degrees Celsius.
        
    Returns:
        dict: A new dictionary with the same keys, but values converted to Fahrenheit.
              Formula used: F = C * 9/5 + 32
              
    Raises:
        TypeError: If any temperature value is not a numeric type (int or float).
    """
    celsius_dict = {}
    
    for location, temp in temperature_dict.items():
        if isinstance(temp, (int, float)):
            fahrenheit_temp = round((temp * 9 / 5) + 32)
            celsius_dict[location] = fahrenheit_temp
        else:
            raise TypeError(f"Temperature value for '{location}' is not a number. Got {type(temp).__name__}")
            
    return celsius_dict

if __name__ == '__main__':
    # Hard-coded sample data with no user input, arguments, or file access required
    temperatures_celsius = {
        "New York": 25,
        "London": 18.5,
        "Tokyo": 30.2,
        "Sydney": 14
    }

    converted_temperatures = celsius_to_fahrenheit(temperatures_celsius)

    print("Original Temperatures (C):")
    for location, temp in temperatures_celsius.items():
        print(f"{location}: {temp}°C")

    print("\nConverted Temperatures (F):")
    for location, temp in converted_temperatures.items():
        print(f"{location}: {temp}°F")