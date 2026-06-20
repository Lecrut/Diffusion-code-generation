def kelvin_to_celsius(temperatures):
    results = []
    for temp in temperatures:
        if not isinstance(temp, (int, float)):
            raise TypeError(f"Expected numeric type, got {type(temp).__name__}")
        if temp < 0:
            raise ValueError("Temperature in Kelvin cannot be negative")
        celsius = temp - 273.15
        results.append(celsius)
    return results

if __name__ == '__main__':
    k_temps = [0, 273.15, 373.15, 1000]
    c_temps = kelvin_to_celsius(k_temps)
    print(c_temps)