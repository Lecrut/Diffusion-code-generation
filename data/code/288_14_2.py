def temperature_conversions():
    conversion_map = {
        'C': {'to_K': lambda t: t + 273.15, 'from_K': lambda t: t - 273.15},
        'F': {'to_K': lambda t: (t - 32) * 5/9 + 273.15, 'from_K': lambda t: (t - 273.15) * 9/5 + 32},
        'K': {'to_C': lambda t: t - 273.15, 'from_C': lambda t: t + 273.15}
    }
    def convert(value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale not in conversion_map or to_scale not in conversion_map:
            raise ValueError("Invalid temperature scale specified.")
        if from_scale == 'C' and to_scale == 'K':
            return conversion_map['C']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'C':
            return conversion_map['K']['from_C'](value)
        elif from_scale == 'F' and to_scale == 'K':
            return conversion_map['F']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'F':
            return conversion_map['K']['from_F'](value)                                                                                                                 
        if from_scale == 'C':
            k = conversion_map['C']['to_K'](value)
            if to_scale == 'K':
                return k
            elif to_scale == 'F':
                return (k - 273.15) * 9/5 + 32
        elif from_scale == 'F':
            k = conversion_map['F']['to_K'](value)
            if to_scale == 'K':
                return k
            elif to_scale == 'C':
                return k - 273.15
        elif from_scale == 'K':
            if to_scale == 'C':
                return conversion_map['K']['from_C'](value)
            elif to_scale == 'F':
                c = conversion_map['K']['from_C'](value)
                return (c + 32) * 5/9
        raise NotImplementedError("Conversion path not implemented for this pair.")
    def bidirectional_convert(value, scale1, scale2):
        if scale1 == scale2:
            return value
        if scale1 in ['C', 'F', 'K'] and scale2 in ['C', 'F', 'K']:
            if scale1 == 'C' and scale2 == 'F':
                k = conversion_map['C']['to_K'](value)
                return (k - 273.15) * 9/5 + 32
            elif scale1 == 'F' and scale2 == 'C':
                k = conversion_map['F']['to_K'](value)
                return k - 273.15
            elif scale1 == 'K' and scale2 == 'C':
                return conversion_map['K']['from_C'](value)
            elif scale1 == 'C' and scale2 == 'K':
                return conversion_map['C']['to_K'](value)
            elif scale1 == 'K' and scale2 == 'C':
                return conversion_map['K']['from_C'](value)
            elif scale1 == 'F' and scale2 == 'K':
                return conversion_map['F']['to_K'](value)
            elif scale1 == 'K' and scale2 == 'F':
                c = conversion_map['K']['from_C'](value)
                return (c + 32) * 5/9
        raise ValueError("Unsupported or invalid scale combination.")
    return bidirectional_convert
if __name__ == '__main__':
    converter = temperature_conversions()
    temp_c = 25.0
    temp_k = converter(temp_c, 'C', 'K')
    print(f"{temp_c}°C is {temp_k:.2f}K")
    temp_f = 68.0
    temp_c_from_f = converter(temp_f, 'F', 'C')
    print(f"{temp_f}°F is {temp_c_from_f:.2f}°C")
    temp_k = 300.0
    temp_f_from_k = converter(temp_k, 'K', 'F')
    print(f"{temp_k}K is {temp_f_from_k:.2f}°F")
    temp_c_to_f = converter(30.0, 'C', 'F')
    print(f"30.0°C is {temp_c_to_f:.2f}°F")
    temp_k_same = converter(100.0, 'K', 'K')
    print(f"100.0K is {temp_k_same:.2f}K")