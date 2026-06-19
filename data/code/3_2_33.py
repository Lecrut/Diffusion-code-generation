def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

def convert_temperatures(temperature_readings):
    return {location: celsius_to_fahrenheit(temp) for location, temp in temperature_readings.items()}

if __name__ == '__main__':
    sample_temperatures = {
        'New York': 10,
        'Los Angeles': 25,
        'Chicago': 15
    }
    converted_temperatures = convert_temperatures(sample_temperatures)
    print(converted_temperatures)