def kelvin_to_celsius(temps):
    results = []
    for t in temps:
        try:
            if not isinstance(t, (int, float)):
                raise TypeError
            c = round(float(t) - 273.15, 2)
            if c < -273.15:
                results.append(None)
            else:
                results.append(c)
        except (TypeError, ValueError):
            results.append(None)
    return results

if __name__ == '__main__':
    sample_data = [0, 273.15, 300.5, -10, "invalid", 400]
    output = kelvin_to_celsius(sample_data)
    print(output)