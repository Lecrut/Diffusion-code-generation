def convert_temperature(temperature, from_unit, to_unit):
    if from_unit == to_unit:
        return temperature
    if from_unit == 'c' and to_unit == 'f':
        return (temperature * 9/5) + 32
    elif from_unit == 'f' and to_unit == 'c':
        return (temperature - 32) * 5/9
    elif from_unit == 'c' and to_unit == 'k':
        return temperature + 273.15
    elif from_unit == 'k' and to_unit == 'c':
        return temperature - 273.15
    else:
        raise ValueError("Unsupported temperature unit conversion.")
if __name__ == '__main__':
    temp_c = 20.0
    temp_f = 68.0
    temp_k = 293.15
    print(f"20.0 C to F: {convert_temperature(temp_c, 'c', 'f')}")
    print(f"68.0 F to C: {convert_temperature(temp_f, 'f', 'c')}")
    print(f"293.15 K to C: {convert_temperature(temp_k, 'k', 'c')}")
    print(f"100.0 C to C: {convert_temperature(100.0, 'c', 'c')}")
    try:
        convert_temperature(100.0, 'c', 'x')
    except ValueError as e:
        print(f"Error caught: {e}")