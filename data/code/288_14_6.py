def temperature_conversions():
    conversion_map = {
        'C': {'to_F': lambda t: (t * 9/5) + 32, 'to_K': lambda t: t + 273.15},
        'F': {'to_C': lambda t: (t - 32) * 5/9, 'to_K': lambda t: (t - 32) * 5/9 + 273.15},
        'K': {'to_C': lambda t: t - 273.15, 'to_F': lambda t: (t - 273.15) * 9/5 + 32},
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
            raise NotImplementedError(f"Conversion from {from_scale} to {to_scale} is not implemented.")
    return conversion_map, convert
if __name__ == '__main__':
    conversion_data, converter = temperature_conversions()
    print("--- Temperature Conversion System ---")
    temp_c = 25.0
    scale1 = 'C'
    scale2 = 'F'
    result1 = converter(temp_c, scale1, scale2)
    print(f"\nConverting {temp_c}°{scale1} to {result1}°{scale2}: {result1:.2f}")
    temp_f = 68.0
    scale1 = 'F'
    scale2 = 'C'
    result2 = converter(temp_f, scale1, scale2)
    print(f"Converting {temp_f}°{scale1} to {result2}°{scale2}: {result2:.2f}")
    temp_c = 100.0
    scale1 = 'C'
    scale2 = 'K'
    result3 = converter(temp_c, scale1, scale2)
    print(f"Converting {temp_c}°{scale1} to {result3}°{scale2}: {result3:.2f}")
    temp_k = 300.0
    scale1 = 'K'
    scale2 = 'F'
    result4 = converter(temp_k, scale1, scale2)
    print(f"Converting {temp_k}°{scale1} to {result4}°{scale2}: {result4:.2f}")
    temp_c = 50.0
    scale1 = 'C'
    scale2 = 'C'
    result5 = converter(temp_c, scale1, scale2)
    print(f"Converting {temp_c}°{scale1} to {result5}°{scale2}: {result5:.2f}")