FAHRENHEIT_CONVERSION_FACTOR = 9/5
FREEZING_POINT_CELSIUS = 0

def convert_temp(celsius_list):
    return [c * FAHRENHEIT_CONVERSION_FACTOR + (32 - FREEZING_POINT_CELSIUS) for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 25, 100]
    fahrenheit_readings = convert_temp(sample_temperatures)
    print(fahrenheit_readings)