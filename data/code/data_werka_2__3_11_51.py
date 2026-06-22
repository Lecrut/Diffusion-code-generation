def celsius_to_fahrenheit(celsius_list):
    CONVERSION_FACTOR = 9 / 5
    BASE_TEMPERATURE = 32
    return [c * CONVERSION_FACTOR + BASE_TEMPERATURE for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [25, -10, 100, 36.8]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)