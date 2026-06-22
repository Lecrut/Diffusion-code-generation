def celsius_to_fahrenheit_readings(temperatures):
    result = {}
    for location, temp_c in temperatures.items():
        temp_f = (temp_c * 9 / 5) + 32
        result[location] = temp_f
    return result

if __name__ == '__main__':
    sample_data = {
        "London": 20.0,
        "Tokyo": 25.5,
        "New York": 15.0,
        "Sydney": -5.0
    }
    converted_data = celsius_to_fahrenheit_readings(sample_data)
    print(converted_data)