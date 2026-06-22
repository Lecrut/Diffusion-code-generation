UNIT_FACTORS = {
    'C_to_F': (9.0 / 5.0, 32.0),
    'F_to_C': (5.0 / 9.0, -32.0),
    'K_to_C': (1.0, -273.15)
}

def celsius_to_fahrenheit(celsius):
    factor, offset = UNIT_FACTORS['C_to_F']
    return celsius * factor + offset

def fahrenheit_to_celsius(fahrenheit):
    factor, offset = UNIT_FACTORS['F_to_C']
    return (fahrenheit + offset) * factor

def kelvin_to_celsius(kelvin):
    factor, offset = UNIT_FACTORS['K_to_C']
    return kelvin * factor + offset

if __name__ == '__main__':
    sample_c = 25.0
    sample_f = 77.0
    sample_k = 300.0
    
    print(celsius_to_fahrenheit(sample_c))
    print(fahrenheit_to_celsius(sample_f))
    print(kelvin_to_celsius(sample_k))