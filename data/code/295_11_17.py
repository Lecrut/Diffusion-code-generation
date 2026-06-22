TEMPERATURE_CONVERSION = {
    'C_to_F': lambda c: (c * 9/5) + 32,
    'F_to_C': lambda f: (f - 32) * 5/9
}

def convert_temperature(value, scale):
    if scale in TEMPERATURE_CONVERSION:
        return TEMPERATURE_CONVERSION[scale](value)
    else:
        raise ValueError("Invalid temperature scale")

if __name__ == '__main__':
    celsius = 25.0
    fahrenheit = convert_temperature(celsius, 'C_to_F')
    print(f"{celsius} C is {fahrenheit:.2f} F")
    
    fahrenheit = 77.0
    celsius = convert_temperature(fahrenheit, 'F_to_C')
    print(f"{fahrenheit} F is {celsius:.2f} C")