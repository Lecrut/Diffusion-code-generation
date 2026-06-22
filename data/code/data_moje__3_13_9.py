def convert_kelvin_to_celsius(temperatures):
    result = []
    for value in temperatures:
        try:
            temp = float(value)
            if temp < 0:
                result.append(None)
            else:
                result.append(temp - 273.15)
        except (ValueError, TypeError):
            result.append(None)
    return result

if __name__ == '__main__':
    test_data = [0, 273.15, 300.0, -10, "invalid", None, 500.5]
    converted = convert_kelvin_to_celsius(test_data)
    print(converted)