def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'c' and to_unit == 'f':
        return (value * 9/5) + 32
    elif from_unit == 'f' and to_unit == 'c':
        return (value - 32) * 5/9
    elif from_unit == 'c' and to_unit == 'k':
        return value + 273.15
    elif from_unit == 'k' and to_unit == 'c':
        return value - 273.15
    else:
        raise ValueError("Unsupported temperature conversion: Invalid unit combination.")
if __name__ == '__main__':
    sample_temp = 25.0
    from_unit = 'c'
    to_unit = 'f'
    result = convert_temperature(sample_temp, from_unit, to_unit)
    print(f"{sample_temp}°{from_unit} is {result:.2f}°{to_unit}")
    sample_temp_k = 300.0
    from_unit_k = 'k'
    to_unit_c = 'c'
    result_k = convert_temperature(sample_temp_k, from_unit_k, to_unit_c)
    print(f"{sample_temp_k}°{from_unit_k} is {result_k:.2f}°{to_unit_c}")
    sample_temp_f = 68.0
    from_unit_f = 'f'
    to_unit_c_2 = 'c'
    result_f = convert_temperature(sample_temp_f, from_unit_f, to_unit_c_2)
    print(f"{sample_temp_f}°{from_unit_f} is {result_f:.2f}°{to_unit_c_2}")
    sample_temp_c = 100.0
    from_unit_c = 'c'
    to_unit_c_2 = 'c'
    result_same = convert_temperature(sample_temp_c, from_unit_c, to_unit_c_2)
    print(f"{sample_temp_c}°{from_unit_c} is {result_same:.2f}°{to_unit_c_2}")