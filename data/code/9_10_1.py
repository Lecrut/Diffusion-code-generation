import math
def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'L': 1.0,
        'mL': 1000.0,
        'm3': 1000.0,
        'gal': 3.78541,
        'L': 1.0,
        'mL': 1000.0,
        'm3': 1000.0,
        'gal': 3.78541
    }
    if from_unit == to_unit:
        return value
    if from_unit == 'L':
        if to_unit == 'mL':
            return value * 1000.0
        elif to_unit == 'm3':
            return value / 1000.0
        elif to_unit == 'gal':
            return value / 3.78541
    elif from_unit == 'mL':
        if to_unit == 'L':
            return value / 1000.0
        elif to_unit == 'm3':
            return value / 1000000.0
        elif to_unit == 'gal':
            return value / 3785.41
    elif from_unit == 'm3':
        if to_unit == 'L':
            return value * 1000.0
        elif to_unit == 'mL':
            return value * 1000000.0
        elif to_unit == 'gal':
            return value * 264.172
    elif from_unit == 'gal':
        if to_unit == 'L':
            return value * 3.78541
        elif to_unit == 'mL':
            return value * 3785.41
        elif to_unit == 'm3':
            return value * 0.00378541
    else:
        return None
def main():
    volume_value = 10.0
    from_unit = 'L'
    to_unit = 'gal'
    result = convert_volume(volume_value, from_unit, to_unit)
    print(f"Original Value: {volume_value} {from_unit}")
    print(f"Converted Value: {result:.4f} {to_unit}")
if __name__ == '__main__':
    main()