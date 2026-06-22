def celsius_to_fahrenheit(temps):
    return {loc: temp * 9/5 + 32 for loc, temp in temps.items()}

if __name__ == '__main__':
    sample_temps = {'New York': 20.0, 'London': 15.5, 'Tokyo': 30.0}
    result = celsius_to_fahrenheit(sample_temps)
    print(result)