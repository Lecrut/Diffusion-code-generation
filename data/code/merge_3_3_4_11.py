def celsius_to_fahrenheit(celcius: dict) -> dict:
    """
    Converts a dictionary of temperature readings from Celsius to Fahrenheit.
    
    Args:
        celcius (dict): A dictionary where keys are locations and values are temperatures in degrees Celsius.
        
    Returns:
        dict: A new dictionary with the same keys but values converted to degrees Fahrenheit.
    """
    return {location: (temp * 9 / 5) + 32 for location, temp in celcius.items()}

if __name__ == '__main__':
    sample_readings = {
        "New York": 20,
        "London": -5,
        "Tokyo": 15
    }
    
    converted_readings = celsius_to_fahrenheit(sample_readings)
    
    print("Original Readings (Celsius):")
    for location, temp in sample_readings.items():
        print(f"{location}: {temp}°C")
        
    print("\nConverted Readings (Fahrenheit):")
    for location, temp in converted_readings.items():
        print(f"{location}: {temp:.2f}°F")