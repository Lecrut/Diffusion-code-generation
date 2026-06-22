def convert_to_celsius(fahrenheit):
    if not isinstance(fahrenheit, tuple):
        raise ValueError("Input must be a tuple of temperatures in Fahrenheit.")
    return tuple(map(lambda f: (f - 32) * 5 / 9, fahrenheit))

if __name__ == '__main__':
    sample_temperatures = (0, 32, 68, 100)
    celsius_temperatures = convert_to_celsius(sample_temperatures)
    print(celsius_temperatures)