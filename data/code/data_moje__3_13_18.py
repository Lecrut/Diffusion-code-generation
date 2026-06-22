def kelvin_to_celsius(temperatures):
    result = []
    for t in temperatures:
        try:
            t_float = float(t)
            if t_float < 0:
                result.append(None)
            else:
                result.append(t_float - 273.15)
        except (TypeError, ValueError):
            result.append(None)
    return result

if __name__ == '__main__':
    sample_data = [0, 273.15, 300.5, -10, "invalid", 1000.0]
    converted = kelvin_to_celsius(sample_data)
    print(converted)