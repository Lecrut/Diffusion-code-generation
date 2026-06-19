def convert_celsius_to_fahrenheit(temperature_readings):
    fahrenheit_readings = {}
    for location, celsius in temperature_readings.items():
        fahrenheit = (celsius * 9/5) + 32
        fahrenheit_readings[location] = fahrenheit
    return fahrenheit_readings

if __name__ == '__main__':
    sample_temperatures = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': 15,
        'Houston': 30
    }
    
    converted_temperatures = convert_celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)