def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

def convert_temperatures(temperatures):
    converted = {}
    for location, temp in temperatures.items():
        converted[location] = celsius_to_fahrenheit(temp)
    return converted

if __name__ == '__main__':
    sample_temperatures = {
        "New York": 20.0,
        "London": 15.5,
        "Tokyo": 25.0,
        "Sydney": 30.0
    }
    result = convert_temperatures(sample_temperatures)
    print(result)