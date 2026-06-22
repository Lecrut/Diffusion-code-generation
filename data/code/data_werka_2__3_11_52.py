def celsius_to_fahrenheit(celsius_list):
    return [convert_celsius_to_fahrenheit(temp) for temp in celsius_list]

def convert_celsius_to_fahrenheit(celsius):
    conversion_factor = 9 / 5
    base_temperature = 32
    return celsius * conversion_factor + base_temperature

if __name__ == '__main__':
    sample_temperatures = [25, -10, 100, 30]
    fahrenheit_temperatures = celsius_to_fahrenheit(sample_temperatures)
    print(fahrenheit_temperatures)