FAHRENHEIT_TO_CELSIUS_CONVERSION_FACTOR = 5 / 9
FREEZING_POINT_FAHRENHEIT = 32

def convert_to_celsius(fahrenheit):
    return tuple(map(lambda f: (f - FREEZING_POINT_FAHRENHEIT) * FAHRENHEIT_TO_CELSIUS_CONVERSION_FACTOR, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (50, 72, 98.6, 32)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)