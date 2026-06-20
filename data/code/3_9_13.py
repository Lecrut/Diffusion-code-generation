def convert_temp(celsius_list):
    return [c * 9/5 + 32 for c in celsius_list]

if __name__ == '__main__':
    sample_temps = [0, 100, 37, -40]
    result = convert_temp(sample_temps)
    print(result)