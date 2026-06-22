CONVERSION_TABLE = {('pascal', 'psi'): 0.000145038, ('psi', 'pascal'): 6894.76, ('pascal', 'atmosphere'): 9.86923e-06, ('atmosphere', 'pascal'): 101325}

def convert_pressure(value, from_unit, to_unit):
    if (from_unit, to_unit) in CONVERSION_TABLE:
        return value * CONVERSION_TABLE[from_unit, to_unit]
    else:
        raise ValueError(f'Unsupported conversion from {from_unit} to {to_unit}')
if __name__ == '__main__':
    print(convert_pressure(100, 'pascal', 'psi'))
    print(convert_pressure(1, 'atmosphere', 'pascal'))