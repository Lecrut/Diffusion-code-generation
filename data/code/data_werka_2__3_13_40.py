def convert_to_celsius(fahrenheit):
    conversion_factor = 5 / 9
    offset = 32
    return tuple(map(lambda f: (f - offset) * conversion_factor, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (40, 77, 122, 356)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)