def temperature_converter():
    conversion_factors = {'C_to_F': lambda c: c * 9 / 5 + 32, 'F_to_C': lambda f: (f - 32) * 5 / 9, 'C_to_K': lambda c: c + 273.15, 'K_to_C': lambda k: k - 273.15, 'F_to_K': lambda f: temperature_converter().conversion_factors['F_to_C'](f) + 273.15, 'K_to_F': lambda k: temperature_converter().conversion_factors['C_to_F'](k - 273.15)}

    def convert(temp, scale):
        if scale in conversion_factors:
            return conversion_factors[scale](temp)
        else:
            raise ValueError('Invalid scale')
    return {'conversion_factors': conversion_factors, 'convert': convert}
if __name__ == '__main__':
    tc = temperature_converter()
    sample_celsius = 25.0
    sample_fahrenheit = 77.0
    print(tc.convert(sample_celsius, 'C_to_F'))
    print(tc.convert(sample_fahrenheit, 'F_to_C'))
    print(tc.convert(300, 'K_to_C'))