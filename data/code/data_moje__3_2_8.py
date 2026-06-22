def celsius_to_fahrenheit(temps):
    return {location: (temp * 9 / 5) + 32 for location, temp in temps.items()}

if __name__ == '__main__':
    sample_temps = {'New York': 20, 'London': 15, 'Tokyo': 25}
    converted_temps = celsius_to_fahrenheit(sample_temps)
    print(converted_temps)