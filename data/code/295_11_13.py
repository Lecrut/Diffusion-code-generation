temp_conversions = {
    'C_to_F': lambda c: (c * 9/5) + 32,
    'F_to_C': lambda f: (f - 32) * 5/9
}

def convert_temperature(value, scale):
    return temp_conversions[scale](value)

if __name__ == '__main__':
    celsius = 20.0
    fahrenheit = convert_temperature(celsius, 'C_to_F')
    print(f"{celsius}°C is {fahrenheit:.1f}°F")

    fahrenheit = 68.0
    celsius = convert_temperature(fahrenheit, 'F_to_C')
    print(f"{fahrenheit}°F is {celsius:.1f}°C")