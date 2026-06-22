TEMPERATURE_CONVERSION = {c: (c * 9/5) + 32 for c in range(-40, 101)}

def convert_temperatures(celsius_list):
    return [TEMPERATURE_CONVERSION[c] for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [-40, -10, 0, 10, 25, 30]
    fahrenheit_temps = convert_temperatures(sample_temps)
    print(fahrenheit_temps)