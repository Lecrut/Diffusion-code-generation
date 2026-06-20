def celsius_to_fahrenheit(temperatures):
    result = {}
    for location, celsius in temperatures.items():
        fahrenheit = celsius * 9 / 5 + 32
        result[location] = fahrenheit
    return result

if __name__ == '__main__':
    readings = {
        'New York': 25.0,
        'London': 15.0,
        'Tokyo': 30.0
    }
    converted = celsius_to_fahrenheit(readings)
    print(converted)