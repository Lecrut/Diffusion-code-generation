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
        if from_scale == 'K':
            kelvin = value
        elif from_scale == 'C':
            kelvin = value + 273.15
        elif from_scale == 'F':
            kelvin = (value - 32) * 5/9 + 273.15
        else:
            raise ValueError(f"Unsupported source scale: {from_scale}")
        if to_scale == 'K':
            result = kelvin
        elif to_scale == 'C':
            result = kelvin - 273.15
        elif to_scale == 'F':
            result = (kelvin - 273.15) * 9/5 + 32
        else:
            raise ValueError(f"Unsupported target scale: {to_scale}")
        return result
    def bidirectional_convert(value, from_scale, to_scale):
        if from_scale == to_scale:
            return value
        if from_scale not in conversion_map or to_scale not in conversion_map:
            raise ValueError("Invalid temperature scale specified.")
        if from_scale == 'K':
            kelvin = value
        elif from_scale == 'C':
            kelvin = value + 273.15
        elif from_scale == 'F':
            kelvin = (value - 32) * 5/9 + 273.15
        else:
            raise ValueError(f"Unsupported source scale: {from_scale}")
        if to_scale == 'K':
            result = kelvin
        elif to_scale == 'C':
            result = kelvin - 273.15
        elif to_scale == 'F':
            result = (kelvin - 273.15) * 9/5 + 32
        else:
            raise ValueError(f"Unsupported target scale: {to_scale}")
        return result
    return bidirectional_convert
if __name__ == '__main__':
    converter = temperature_conversions()
    celsius_temp = 25.0
    fahrenheit_result = converter(celsius_temp, 'C', 'F')
    print(f"{celsius_temp}°C is {fahrenheit_result:.2f}°F")
    fahrenheit_temp = 77.0
    celsius_result = converter(fahrenheit_temp, 'F', 'C')
    print(f"{fahrenheit_temp}°F is {celsius_result:.2f}°C")
    kelvin_temp = 300.0
    celsius_from_k = converter(kelvin_temp, 'K', 'C')
    print(f"{kelvin_temp}°K is {celsius_from_k:.2f}°C")
    kelvin_from_f = converter(68.0, 'F', 'K')
    print(f"68.0°F is {kelvin_from_f:.2f}°K")
    self_test = converter(100.0, 'K', 'K')
    print(f"100.0°K is {self_test:.2f}°K")