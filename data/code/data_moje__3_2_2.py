def celsius_to_fahrenheit(temperatures):
    return {loc: temp * 9 / 5 + 32 for loc, temp in temperatures.items()}

if __name__ == '__main__':
    sample_temps = {'New York': 10, 'London': 15, 'Tokyo': 25}
    result = celsius_to_fahrenheit(sample_temps)
    print(result)