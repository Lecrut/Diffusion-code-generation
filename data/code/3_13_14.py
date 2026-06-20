def convert_kelvin_to_celsius(readings):
    result = []
    for value in readings:
        try:
            celsius = float(value) - 273.15
            result.append(celsius)
        except (TypeError, ValueError):
            result.append(None)
    return result

if __name__ == '__main__':
    test_data = [0, 273.15, 300, -5, "invalid", None]
    converted_values = convert_kelvin_to_celsius(test_data)
    print(converted_values)