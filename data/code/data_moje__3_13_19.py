def kelvin_to_celsius(kelvin_values):
    celsius_values = []
    for k in kelvin_values:
        try:
            k = float(k)
            if k < 0:
                celsius_values.append(None)
            else:
                celsius_values.append(k - 273.15)
        except (TypeError, ValueError):
            celsius_values.append(None)
    return celsius_values
if __name__ == '__main__':
    test_data = [0, 273.15, 300, 1000, -10, 'invalid', None, 20, 500.5]
    result = kelvin_to_celsius(test_data)
    print(result)