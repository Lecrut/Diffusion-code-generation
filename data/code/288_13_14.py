def celsius_to_fahrenheit(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures_celsius = [0, 100, -40]
    temperatures_fahrenheit = celsius_to_fahrenheit(sample_temperatures_celsius)
    print(temperatures_fahrenheit)