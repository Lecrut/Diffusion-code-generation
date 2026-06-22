def celsius_to_fahrenheit(temperatures):
    return {location: (temp * 9/5) + 32 for location, temp in temperatures.items()}

if __name__ == '__main__':
    sample_temps = {
        'New York': 20.0,
        'London': 15.5,
        'Tokyo': 25.0,
        'Sydney': 30.0
    }
    result = celsius_to_fahrenheit(sample_temps)
    print(result)