def celsius_to_fahrenheit(celcius_dict: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celcius_dict (dict): A dictionary where keys are location names and 
                            values are temperatures in degrees Celsius as floats or ints.
                            
    Returns:
        dict: A new dictionary with the same keys but values converted to Fahrenheit.
              Formula used: F = C * 9/5 + 32
    """
    fahrenheit_dict = {}
    
    for location, celsius_temp in celcius_dict.items():
        # Convert Celsius to Fahrenheit using the formula (C × 1.8) + 32
        fahrenheit_temp = round((celsius_temp * 9 / 5) + 32, 2)
        fahrenheit_dict[location] = fahrenheit_temp
        
    return fahrenheit_dict

if __name__ == '__main__':
    # Hard-coded sample temperature readings in Celsius
    temperature_readings_celsius = {
        "New York": 25.0,
        "London": 18,
        "Tokyo": -3.5,
        "Sydney": 14.75,
        "Paris": 19
    }

    # Convert temperatures to Fahrenheit and store in a new dictionary
    converted_temperatures = celsius_to_fahrenheit(temperature_readings_celsius)

    # Print the result for verification (no user input required)
    print("Temperature readings converted from Celsius to Fahrenheit:")
    for location, temp_fah in converted_temperatures.items():
        print(f"{location}: {temp_fah}°F")