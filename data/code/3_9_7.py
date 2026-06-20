def convert_temp(celsius_readings):
    return [c * 9 / 5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    sample_temperatures = [0, 10, 25, 37, 100]
    result = convert_temp(sample_temperatures)
    print(result)