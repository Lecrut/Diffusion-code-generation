def kelvin_to_celsius(temperatures):
    celsius_values = []
    for temp in temperatures:
        if not isinstance(temp, (int, float)):
            continue
        if temp < 0:
            celsius_values.append(None)
        else:
            celsius_values.append(temp - 273.15)
    return celsius_values

if __name__ == '__main__':
    sample_temps = [0, 273.15, 300.15, -10, 'invalid', 100.5]
    result = kelvin_to_celsius(sample_temps)
    print(result)