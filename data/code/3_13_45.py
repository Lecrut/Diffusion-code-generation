def convert_to_celsius(fahrenheit):
    conversion_factor = 5 / 9
    offset = 32
    return tuple(map(lambda f: (f - offset) * conversion_factor, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (0, 32, 68, 100)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)