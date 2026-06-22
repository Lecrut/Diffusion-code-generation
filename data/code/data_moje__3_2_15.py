def celsius_to_fahrenheit_readings(readings):
    return {location: (temp * 9 / 5) + 32 for location, temp in readings.items()}

if __name__ == '__main__':
    sample_readings = {'London': 20, 'Tokyo': 25, 'NewYork': -5}
    result = celsius_to_fahrenheit_readings(sample_readings)
    print(result)