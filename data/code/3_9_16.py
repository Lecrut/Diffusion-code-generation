def convert_temp(celsius_readings):
    return [(c * 9 / 5) + 32 for c in celsius_readings]

if __name__ == '__main__':
    sample_temps = [0, 10, 20, 37, 100, -40]
    print(convert_temp(sample_temps))