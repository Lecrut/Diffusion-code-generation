def convert_temp(celsius_readings):
    return [c * 9/5 + 32 for c in celsius_readings]

if __name__ == '__main__':
    sample_temperatures = [-40, 0, 25, 100, 212]
    result = convert_temp(sample_temperatures)
    print(result)