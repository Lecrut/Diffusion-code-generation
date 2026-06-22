def kelvin_to_celsius(kelvin_values):
    results = []
    for k in kelvin_values:
        try:
            k = float(k)
            if k < 0:
                raise ValueError("Temperature in Kelvin cannot be negative")
            c = k - 273.15
            results.append(c)
        except (ValueError, TypeError):
            results.append(None)
    return results

if __name__ == '__main__':
    sample_temps = [300, 0, 273.15, -10, 'invalid', 1000]
    print(kelvin_to_celsius(sample_temps))