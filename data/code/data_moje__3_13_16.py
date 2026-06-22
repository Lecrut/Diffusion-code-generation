def kelvin_to_celsius(temperatures):
    results = []
    for temp in temperatures:
        if not isinstance(temp, (int, float)):
            continue
        if temp < 0:
            results.append(None)
        else:
            results.append(temp - 273.15)
    return results

if __name__ == '__main__':
    sample_data = [0, 273.15, 300, -10, "invalid", 1000.5]
    converted = kelvin_to_celsius(sample_data)
    print(converted)