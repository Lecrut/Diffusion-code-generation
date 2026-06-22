CONVERSION_FACTOR_C_TO_F = 9 / 5
OFFSET_C_TO_F = 32

def celsius_to_fahrenheit(celsius):
    return int(celsius * CONVERSION_FACTOR_C_TO_F + OFFSET_C_TO_F)

def fahrenheit_to_celsius(fahrenheit):
    return int((fahrenheit - OFFSET_C_TO_F) * (5 / CONVERSION_FACTOR_C_TO_F))
if __name__ == '__main__':
    sample_celsius = 25
    print(celsius_to_fahrenheit(sample_celsius))
    sample_fahrenheit = 77
    print(fahrenheit_to_celsius(sample_fahrenheit))