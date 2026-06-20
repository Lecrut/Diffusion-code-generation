def kelvin_to_celsius(kelvin_values):
    celsius_values = []
    for k in kelvin_values:
        try:
            if not isinstance(k, (int, float)):
                raise TypeError('Value must be a number')
            if k < 0:
                raise ValueError('Temperature in Kelvin cannot be negative')
            celsius_values.append(k - 273.15)
        except (TypeError, ValueError):
            celsius_values.append(None)
    return celsius_values
if __name__ == '__main__':
    test_values = [300.15, 0, 273.15, 1000, -50, 'invalid', None, 100.0]
    result = kelvin_to_celsius(test_values)
    print(result)