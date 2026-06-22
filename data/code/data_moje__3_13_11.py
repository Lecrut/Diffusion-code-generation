def kelvin_to_celsius(temperatures):
    if not isinstance(temperatures, list):
        return []
    
    result = []
    for temp in temperatures:
        try:
            numeric_val = float(temp)
            if numeric_val < 0:
                result.append(None)
            else:
                celsius = numeric_val - 273.15
                result.append(celsius)
        except (TypeError, ValueError):
            result.append(None)
    return result

if __name__ == '__main__':
    sample_temps = [0, 273.15, 373.15, -1, 'invalid', None, 100]
    converted = kelvin_to_celsius(sample_temps)
    print(converted)