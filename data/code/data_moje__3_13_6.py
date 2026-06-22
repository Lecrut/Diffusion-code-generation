def kelvin_to_celsius(readings):
    results = []
    for temp in readings:
        if isinstance(temp, (int, float)) and temp >= 0:
            results.append(temp - 273.15)
        else:
            results.append(None)
    return results

if __name__ == '__main__':
    sample_temps = [0, 273.15, 300.15, -1, 'invalid', None]
    converted = kelvin_to_celsius(sample_temps)
    print(converted)