def celsius_to_fahrenheit(readings):
    result = {}
    for location, celsius in readings.items():
        fahrenheit = (celsius * 9 / 5) + 32
        result[location] = fahrenheit
    return result

if __name__ == '__main__':
    sample_data = {
        "New York": 22.5,
        "London": 18.0,
        "Tokyo": 30.2,
        "Sydney": -5.0
    }
    converted_data = celsius_to_fahrenheit(sample_data)
    print(converted_data)