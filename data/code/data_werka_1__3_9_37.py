CONVERSION_FACTOR = 9 / 5
FREEZING_POINT_CELSIUS = 0
FREEZING_POINT_FAHRENHEIT = 32

def convert_temp(celsius_list):
    return [(c * CONVERSION_FACTOR) + FREEZING_POINT_FAHRENHEIT for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [15, -10, 0, 100]
    fahrenheit_readings = convert_temp(sample_temperatures)
    print(fahrenheit_readings)