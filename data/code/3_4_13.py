def celsius_to_fahrenheit(temperature_dict):
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        temperature_dict (dict): A dictionary where keys are location names 
                                and values are temperatures in degrees Celsius.
        
    Returns:
        dict: A new dictionary with the same keys but values converted to 
              degrees Fahrenheit using the formula F = C * 9/5 + 32.
    
    Raises:
        TypeError: If the input is not a dictionary or if any value is not numeric.
    """
    fahrenheit_dict = {}
    for location, celsius_temp in temperature_dict.items():
        try:
            # Ensure the value is a number (int or float)
            celsius_value = float(celsius_temp)
            # Convert to Fahrenheit
            fahrenheit_value = (celsius_value * 9 / 5) + 32
            fahrenheit_dict[location] = round(fahrenheit_value, 2)
        except ValueError:
            raise TypeError(f"Temperature for location '{location}' is not a valid number.")
    return fahrenheit_dict

if __name__ == '__main__':
    # Hard-coded sample data with no user input or external dependencies
    sample_readings = {
        "New York": 25.0,
        "London": -3.5,
        "Tokyo": 18.75,
        "Sydney": 40.0
    }

    converted_data = celsius_to_fahrenheit(sample_readings)
    
    # Print the result to verify functionality without file I/O or network access
    print("Temperature readings in Fahrenheit:")
    for location, temp in converted_data.items():
        print(f"{location}: {temp}°F")