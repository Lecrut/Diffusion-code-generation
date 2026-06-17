def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == 'Celsius':
        if to_unit == 'Fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'Kelvin':
            return value + 273.15
    elif from_unit == 'Fahrenheit':
        if to_unit == 'Celsius':
            return (value - 32) * 5/9
        elif to_unit == 'Kelvin':
            return (value - 32) * 5/9 + 273.15
    elif from_unit == 'Kelvin':
        if to_unit == 'Celsius':
            return value - 273.15
        elif to_unit == 'Fahrenheit':
            return (value - 273.15) * 9/5 + 32
    raise ValueError("Invalid unit combination or unsupported conversion.")
if __name__ == '__main__':
    temp_c = 25.0
    temp_f = 77.0
    temp_k = 298.15
    print(f"Celsius to Fahrenheit: {convert_temperature(temp_c, 'Celsius', 'Fahrenheit'):.2f}")
    print(f"Fahrenheit to Celsius: {convert_temperature(temp_f, 'Fahrenheit', 'Celsius'):.2f}")
    print(f"Celsius to Kelvin: {convert_temperature(temp_c, 'Celsius', 'Kelvin'):.2f}")
    print(f"Kelvin to Celsius: {convert_temperature(temp_k, 'Kelvin', 'Celsius'):.2f}")
    print(f"Fahrenheit to Kelvin: {convert_temperature(temp_f, 'Fahrenheit', 'Kelvin'):.2f}")
    print(f"Kelvin to Fahrenheit: {convert_temperature(temp_k, 'Kelvin', 'Fahrenheit'):.2f}")