def celsius_to_fahrenheit(celcius_dict):
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celcius_dict (dict): A dictionary where keys are location names 
                            and values are temperatures in degrees Celsius.
                            
    Returns:
        dict: A new dictionary with the same keys but values converted to Fahrenheit.
              Formula used: F = (C * 9/5) + 32
    """
    fahrenheit_dict = {}
    
    for location, celsius_temp in celcius_dict.items():
        # Convert Celsius to Fahrenheit using the formula: F = C * 1.8 + 32
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        fahrenheit_dict[location] = round(fahrenheit_temp, 2)
        
    return fahrenheit_dict

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_readings = {
        "New York": 25.0,
        "London": -5.0,
        "Tokyo": 30.5,
        "Sydney": 18.75
    }

    # Execute the conversion and print results for verification
    converted_readings = celsius_to_fahrenheit(sample_readings)
    
    print("Temperature readings in Fahrenheit:")
    for location, temp in converted_readings.items():
        print(f"{location}: {temp}°F")