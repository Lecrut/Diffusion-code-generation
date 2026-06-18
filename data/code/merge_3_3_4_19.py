import math

def celsius_to_fahrenheit(celsius: float) -> int:
    """Convert a temperature in Celsius to Fahrenheit."""
    return round((celsius * 9 / 5) + 32, -1)

def convert_temperature_readings(temperature_data: dict[str, float]) -> dict[str, int]:
    """
    Convert all temperature readings from Celsius to Fahrenheit.
    
    Args:
        temperature_data: A dictionary where keys are location names and 
                         values are temperatures in Celsius (float).
        
    Returns:
        A new dictionary with the same keys but temperatures converted to 
        Fahrenheit as integers rounded to the nearest whole degree.
    """
    return {location: celsius_to_fahrenheit(temp) for location, temp in temperature_data.items()}

if __name__ == '__main__':
    sample_readings = {
        "New York": 25.0,
        "London": 18.5,
        "Tokyo": 30.2,
        "Sydney": -2.4
    }

    converted_data = convert_temperature_readings(sample_readings)
    
    print("Temperature conversions (Celsius to Fahrenheit):")
    for location, temp in converted_data.items():
        print(f"{location}: {temp}°F")