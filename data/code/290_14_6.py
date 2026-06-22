CONVERSION_FACTOR = {'kg_to_lb': 2.20462, 'lb_to_kg': 1 / 2.20462}

def convert_mass(value, from_unit, to_unit):
    return round(value * CONVERSION_FACTOR[f'{from_unit}_to_{to_unit}'], 2)
if __name__ == '__main__':
    print(convert_mass(1, 'kg', 'lb'))
    print(convert_mass(2.2, 'lb', 'kg'))