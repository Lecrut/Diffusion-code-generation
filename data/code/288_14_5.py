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
            raise ValueError("Invalid temperature scale provided.")
        if from_scale == 'C' and to_scale == 'K':
            return conversion_map['C']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'C':
            return conversion_map['K']['from_C'](value)
        elif from_scale == 'F' and to_scale == 'K':
            return conversion_map['F']['to_K'](value)
        elif from_scale == 'K' and to_scale == 'F':
            return conversion_map['K']['from_F'](value)                                                                                           
        elif from_scale == 'C' and to_scale == 'F':
            return (value * 9/5) + 32
        elif from_scale == 'F' and to_scale == 'C':
            return (value - 32) * 5/9
        else:
            raise NotImplementedError(f"Conversion from {from_scale} to {to_scale} is not implemented.")
    def bidirectional_convert(value, scale1, scale2):
        if scale1 == scale2:
            return value
        if (scale1 == 'C' and scale2 == 'F') or (scale1 == 'F' and scale2 == 'C'):
            if scale1 == 'C':
                return convert(value, 'C', 'F')
            else:
                return convert(value, 'F', 'C')
        if (scale1 == 'C' and scale2 == 'K') or (scale1 == 'K' and scale2 == 'C'):
            if scale1 == 'C':
                return convert(value, 'C', 'K')
            else:
                return convert(value, 'K', 'C')
        if (scale1 == 'F' and scale2 == 'K') or (scale1 == 'K' and scale2 == 'F'):
            if scale1 == 'F':
                return convert(value, 'F', 'K')
            else:
                return convert(value, 'K', 'F')
        raise NotImplementedError(f"Conversion between {scale1} and {scale2} is not supported.")
    return bidirectional_convert
if __name__ == '__main__':
    converter = temperature_conversions()
    temp_c = 25.0
    result_k = converter(temp_c, 'C', 'K')
    print(f"{temp_c}°C is {result_k:.2f}°K")
    temp_k = 300.15
    result_c = converter(temp_k, 'K', 'C')
    print(f"{temp_k}°K is {result_c:.2f}°C")
    temp_f = 68.0
    result_c_from_f = converter(temp_f, 'F', 'C')
    print(f"{temp_f}°F is {result_c_from_f:.2f}°C")
    temp_c_to_f = 100.0
    result_f_from_c = converter(temp_c_to_f, 'C', 'F')
    print(f"{temp_c_to_f}°C is {result_f_from_c:.2f}°F")
    temp_f_to_k = 77.0
    result_k_from_f = converter(temp_f_to_k, 'F', 'K')
    print(f"{temp_f_to_k}°F is {result_k_from_f:.2f}°K")