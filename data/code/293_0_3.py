conversion_table = {'CtoF': lambda c: c * 9 / 5 + 32, 'FtoC': lambda f: (f - 32) * 5 / 9}

def convert_temperature(value, scale):
    return conversion_table[f'{scale}toC'](value) if scale == 'F' else conversion_table['CtoF'](value)
if __name__ == '__main__':
    print(convert_temperature(0, 'C'))
    print(convert_temperature(32, 'F'))