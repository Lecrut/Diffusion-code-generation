def convert_celsius_to_fahrenheit(temperatures):
    return [(c * 9/5) + 32 for c in temperatures]

if __name__ == '__main__':
    sample_temperatures = [0, -40, 100, 37]
    converted_temperatures = convert_celsius_to_fahrenheit(sample_temperatures)
    print(converted_temperatures)