conversion_factors = {'CtoF': lambda c: c * 9 / 5 + 32, 'FtoC': lambda f: (f - 32) * 5 / 9}

def convert_temperature(value, scale):
    return conversion_factors[f'{scale}toC'](value) if scale == 'F' else conversion_factors['CtoF'](value)
if __name__ == '__main__':
    print(convert_temperature(0, 'C'))
    print(convert_temperature(32, 'F'))