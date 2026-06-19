def convert_temp(celsius_list):
    if not celsius_list:
        return []
    return [(c * 9/5) + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [30, -10, 100, 0]
    fahrenheit_temps = convert_temp(sample_temps)
    print(fahrenheit_temps)