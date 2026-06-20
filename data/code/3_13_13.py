def kelvin_to_celsius(kelvin_values):
    results = []
    for k in kelvin_values:
        if isinstance(k, (int, float)):
            if k < 0:
                results.append(None)
            else:
                results.append(k - 273.15)
        else:
            results.append(None)
    return results

if __name__ == '__main__':
    sample_temps = [300, 273.15, 0, -10, 1000, 'invalid', 4.5]
    converted = kelvin_to_celsius(sample_temps)
    print(converted)