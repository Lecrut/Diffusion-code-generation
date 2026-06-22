def convert_kelvin_to_celsius(readings):
    result = []
    for value in readings:
        try:
            num_value = float(value)
            if num_value < 0:
                result.append(None)
            else:
                result.append(num_value - 273.15)
        except (ValueError, TypeError):
            result.append(None)
    return result

if __name__ == '__main__':
    test_data = [0.0, 273.15, 373.15, -10, "invalid", 100]
    converted_values = convert_kelvin_to_celsius(test_data)
    print(converted_values)