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
        elif from_scale == 'C' and to_scale == 'F':
            return (value * 9/5) + 32
        elif from_scale == 'F' and to_scale == 'C':
            return (value - 32) * 5/9
        else:
            raise NotImplementedError(f"Conversion from {from_scale} to {to_scale} is not implemented.")
    return convert
if __name__ == '__main__':
    converter = temperature_conversions()
    celsius_temp = 25.0
    kelvin_result = converter(celsius_temp, 'C', 'K')
    print(f"{celsius_temp}°C is {kelvin_result:.2f}K")
    kelvin_temp = 300.15
    celsius_result = converter(kelvin_temp, 'K', 'C')
    print(f"{kelvin_temp}K is {celsius_result:.2f}°C")
    fahrenheit_temp = 68.0
    celsius_from_f = converter(fahrenheit_temp, 'F', 'C')
    print(f"{fahrenheit_temp}°F is {celsius_from_f:.2f}°C")
    fahrenheit_from_c = converter(celsius_temp, 'C', 'F')
    print(f"{celsius_temp}°C is {fahrenheit_from_c:.2f}°F")
    fahrenheit_to_k = converter(77.0, 'F', 'K')
    print(f"{77.0}°F is {fahrenheit_to_k:.2f}K")