def find_max_temperature_celsius(temperatures):
    max_celsius = max(temperatures)
    return (max_celsius * 9/5) + 32

if __name__ == '__main__':
    sample_temperatures = [15, 20, 25, 30, 35]
    max_temperature_fahrenheit = find_max_temperature_celsius(sample_temperatures)
    print(max_temperature_fahrenheit)