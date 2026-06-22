def celsius_to_fahrenheit_temps(temperatures):
    result = {}
    for location, celsius in temperatures.items():
        fahrenheit = (celsius * 9 / 5) + 32
        result[location] = fahrenheit
    return result

if __name__ == '__main__':
    sample_data = {
        "New York": 20,
        "London": 15,
        "Tokyo": 25,
        "Moscow": -10
    }
    converted_temps = celsius_to_fahrenheit_temps(sample_data)
    print(converted_temps)