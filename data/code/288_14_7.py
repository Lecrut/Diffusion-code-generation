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
            return conversion_map['F']['from_K'](value)
        elif from_scale == 'C' and to_scale == 'F':
            return (value * 9/5) + 32
        elif from_scale == 'F' and to_scale == 'C':
            return (value - 32) * 5/9
        else:
            raise ValueError(f"Conversion not implemented between {from_scale} and {to_scale}")
    return convert, conversion_map
if __name__ == '__main__':
    convert_func, mapping = temperature_conversions()
    print("--- Test Case 1: Celsius to Kelvin ---")
    celsius_temp = 25.0
    kelvin_result = convert_func(celsius_temp, 'C', 'K')
    print(f"{celsius_temp}°C is {kelvin_result:.2f} K")
    print("\n--- Test Case 2: Kelvin to Celsius ---")
    kelvin_temp = 300.15
    celsius_result = convert_func(kelvin_temp, 'K', 'C')
    print(f"{kelvin_temp} K is {celsius_result:.2f} C")
    print("\n--- Test Case 3: Fahrenheit to Kelvin ---")
    fahrenheit_temp = 68.0
    kelvin_result = convert_func(fahrenheit_temp, 'F', 'K')
    print(f"{fahrenheit_temp}°F is {kelvin_result:.2f} K")
    print("\n--- Test Case 4: Celsius to Fahrenheit ---")
    celsius_temp = 100.0
    fahrenheit_result = convert_func(celsius_temp, 'C', 'F')
    print(f"{celsius_temp}°C is {fahrenheit_result:.2f} F")
    print("\n--- Test Case 5: Fahrenheit to Celsius ---")
    fahrenheit_temp = 32.0
    celsius_result = convert_func(fahrenheit_temp, 'F', 'C')
    print(f"{fahrenheit_temp}°F is {celsius_result:.2f} C")