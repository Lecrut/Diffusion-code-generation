CONVERSION_FACTOR = 9/5
OFFSET = 32

def convert_celsius_to_fahrenheit(celsius):
    return celsius * CONVERSION_FACTOR + OFFSET

def find_max_temperature(temperatures):
    max_temp_celsius = max(temperatures)
    return convert_celsius_to_fahrenheit(max_temp_celsius)

if __name__ == '__main__':
    sample_temps = [15, 20, 25, 30, -5, 10]
    print(find_max_temperature(sample_temps))