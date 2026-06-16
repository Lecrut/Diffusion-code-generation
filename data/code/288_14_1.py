def temperature_conversions():
    conversion_map = {
        'C': {'to_F': lambda t: (t * 9/5) + 32, 'to_K': lambda t: t + 273.15, 'from_F': lambda t: (t - 32) * 5/9, 'from_K': lambda t: t - 273.15},
        'F': {'to_C': lambda t: (t - 32) * 5/9, 'to_K': lambda t: (t - 32) * 5/9 + 273.15, 'from_C': lambda t: (t * 9/5) + 32, 'from_K': lambda t: (t - 273.15) * 9/5 + 32},
        'K': {'to_C': lambda t: t - 273.15, 'to_F': lambda t: (t - 273.15) * 9/5 + 32, 'from_C': lambda t: t + 273.15, 'from_F': lambda t: (t - 32) * 5/9},
    }
    def convert(value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale not in conversion_map or to_scale not in conversion_map:
            raise ValueError("Invalid temperature scale specified.")
        if from_scale == 'C':
            if to_scale == 'F': return conversion_map['C']['to_F'](value)
            if to_scale == 'K': return conversion_map['C']['to_K'](value)
        elif from_scale == 'F':
            if to_scale == 'C': return conversion_map['F']['to_C'](value)
            if to_scale == 'K': return conversion_map['F']['to_K'](value)
        elif from_scale == 'K':
            if to_scale == 'C': return conversion_map['K']['to_C'](value)
            if to_scale == 'F': return conversion_map['K']['to_F'](value)
        raise ValueError("Conversion path not found for the specified scales.")
    return conversion_map, convert
if __name__ == '__main__':
    conversion_data, converter = temperature_conversions()
    print("--- Testing Conversions ---")
    temp_c = 25.0
    print(f"{temp_c}°C to °F: {converter(temp_c, 'C', 'F'):.2f}")
    temp_f = 68.0
    print(f"{temp_f}°F to °C: {converter(temp_f, 'F', 'C'):.2f}")
    temp_c_k = 100.0
    print(f"{temp_c_k}°C to K: {converter(temp_c_k, 'C', 'K'):.2f}")
    temp_k = 300.0
    print(f"{temp_k}K to °F: {converter(temp_k, 'K', 'F'):.2f}")
    temp_f_to_k = 77.0
    print(f"{temp_f_to_k}°F to K: {converter(temp_f_to_k, 'F', 'K'):.2f}")
    temp_c_to_c = 50.0
    print(f"{temp_c_to_c}°C to °C: {converter(temp_c_to_c, 'C', 'C'):.2f}")