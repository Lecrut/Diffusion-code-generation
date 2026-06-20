def convert_temp(celsius_readings):
    return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    sample_celsius = [0, 10, 20, 30, 100]
    print(convert_temp(sample_celsius))