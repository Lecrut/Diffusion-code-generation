def convert_kelvin_to_celsius(values):
    result = []
    for value in values:
        try:
            numeric_value = float(value)
            if numeric_value < 0:
                result.append(None)
            else:
                result.append(numeric_value - 273.15)
        except (TypeError, ValueError):
            result.append(None)
    return result

if __name__ == '__main__':
    test_data = [0, 273.15, 373.15, -10, "invalid", 1000.5]
    print(convert_kelvin_to_celsius(test_data))