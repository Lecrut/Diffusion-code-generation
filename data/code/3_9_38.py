def convert_temp(celsius_list):
    return [(c * 9/5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 100, 37]
    fahrenheit_readings = convert_temp(sample_temperatures)
    print(fahrenheit_readings)