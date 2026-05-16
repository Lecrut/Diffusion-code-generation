import math
def convert_volume(value, from_unit, to_unit):
    conversion_factors = {
        'L': 1.0,
        'mL': 0.001,
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
            return value / (1000.0 * 3.78541)
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
        raise ValueError("Invalid source unit specified.")
def main():
    sample_value = 10.0
    from_unit = 'L'
    to_unit = 'gal'
    result = convert_volume(sample_value, from_unit, to_unit)
    print(f"Sample Value: {sample_value} {from_unit}")
    print(f"Conversion to {to_unit}: {result:.4f}")
if __name__ == '__main__':
    main()