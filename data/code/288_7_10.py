CELSIUS_TO_FAHRENHEIT = 9 / 5
FAHRENHEIT_OFFSET = 32

def find_max_temperature_in_fahrenheit(temperatures):
    max_celsius = max(temperatures)
    return (max_celsius * CELSIUS_TO_FAHRENHEIT) + FAHRENHEIT_OFFSET

if __name__ == '__main__':
    sample_temperatures = [25, 30, 18, 40, -5]
    max_temp_fahrenheit = find_max_temperature_in_fahrenheit(sample_temperatures)
    print(max_temp_fahrenheit)