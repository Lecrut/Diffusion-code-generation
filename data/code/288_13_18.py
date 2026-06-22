def celsius_to_fahrenheit(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps_celsius = [0, 100, -40, 37]
    sample_temps_fahrenheit = celsius_to_fahrenheit(sample_temps_celsius)
    print(sample_temps_fahrenheit)