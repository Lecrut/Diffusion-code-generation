TEMPERATURE_CONVERSION = {
    'Fahrenheit': lambda f: (f - 32) * 5 / 9,
}

def convert_to_celsius(fahrenheit_temperatures):
    conversion_function = TEMPERATURE_CONVERSION['Fahrenheit']
    return tuple(map(conversion_function, fahrenheit_temperatures))

if __name__ == '__main__':
    sample_temperatures = (45, 86, 130, 374)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)