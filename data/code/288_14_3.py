def temperature_conversions():
    conversion_map = {
        'C': {'to_F': lambda t: (t * 9/5) + 32, 'to_K': lambda t: t + 273.15},
        'F': {'to_C': lambda t: (t - 32) * 5/9, 'to_K': lambda t: (t + 459.67) * 5/9},
        'K': {'to_C': lambda t: t - 273.15, 'to_F': lambda t: (t - 273.15) * 9/5},
    }
    def convert(value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale not in conversion_map or to_scale not in conversion_map:
            raise ValueError("Invalid temperature scale specified.")
        if from_scale == 'C' and to_scale == 'F':
            return conversion_map['C']['to_F'](value)
        elif from_scale == 'F' and to_scale == 'C':
            return conversion_map['F']['to_C'](value)
        elif from_scale == 'C' and to_scale == 'K':
            return conversion_map['C']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'C':
            return conversion_map['K']['to_C'](value)
        elif from_scale == 'F' and to_scale == 'K':
            return conversion_map['F']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'F':
            return conversion_map['K']['to_F'](value)
        else:
            raise ValueError(f"Conversion from {from_scale} to {to_scale} is not supported.")
    return conversion_map, convert
if __name__ == '__main__':
    conversion_data, converter = temperature_conversions()
    print("--- Conversion Tests ---")
    temp_c = 20.0
    result_cf = converter(temp_c, 'C', 'F')
    print(f"{temp_c}°C is {result_cf:.2f}°F")
    temp_f = 68.0
    result_fc = converter(temp_f, 'F', 'C')
    print(f"{temp_f}°F is {result_fc:.2f}°C")
    temp_c_k = 100.0
    result_ck = converter(temp_c_k, 'C', 'K')
    print(f"{temp_c_k}°C is {result_ck:.2f}K")
    temp_k_c = 300.15
    result_kc = converter(temp_k_c, 'K', 'C')
    print(f"{temp_k_c}K is {result_kc:.2f}°C")
    temp_f_k = 32.0
    result_fk = converter(temp_f_k, 'F', 'K')
    print(f"{temp_f_k}°F is {result_fk:.2f}K")
    temp_f_roundtrip = 50.0
    result_fc_roundtrip = converter(temp_f_roundtrip, 'F', 'C')
    print(f"{temp_f_roundtrip}°F roundtrip to C: {result_fc_roundtrip:.2f}°C")