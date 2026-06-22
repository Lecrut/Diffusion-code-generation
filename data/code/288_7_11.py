def convert_celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temperatures = [15, -10, 0, 30, -40]
    max_temp_celsius = max(sample_temperatures)
    max_temp_fahrenheit = convert_celsius_to_fahrenheit(max_temp_celsius)
    print(f"The maximum temperature is {max_temp_fahrenheit}°F")