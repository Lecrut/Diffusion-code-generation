def convert_temp(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [0, 100, -40, 37]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)