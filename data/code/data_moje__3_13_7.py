def convert_kelvin_to_celsius(values):
    result = []
    for value in values:
        if isinstance(value, (int, float)):
            celsius = value - 273.15
            result.append(celsius)
        else:
            result.append(None)
    return result

if __name__ == '__main__':
    sample_data = [273.15, 0, 300.5, "invalid", -10, 1000.0]
    print(convert_kelvin_to_celsius(sample_data))