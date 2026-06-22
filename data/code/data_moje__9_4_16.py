import argparse

def convert_volume(volume, from_unit, to_unit):
    conversions = {
        ('milliliter', 'liter'): 0.001,
        ('milliliter', 'gallon'): 0.000264172,
        ('milliliter', 'cup'): 0.00422675,
        ('milliliter', 'tablespoon'): 0.067628,
        ('milliliter', 'teaspoon'): 0.202884,
        ('liter', 'milliliter'): 1000,
        ('liter', 'gallon'): 0.264172,
        ('liter', 'cup'): 4.22675,
        ('liter', 'tablespoon'): 67.628,
        ('liter', 'teaspoon'): 202.884,
        ('gallon', 'milliliter'): 3785.41,
        ('gallon', 'liter'): 3.78541,
        ('gallon', 'cup'): 16.0,
        ('gallon', 'tablespoon'): 256.0,
        ('gallon', 'teaspoon'): 768.0,
        ('cup', 'milliliter'): 236.588,
        ('cup', 'liter'): 0.236588,
        ('cup', 'gallon'): 0.0625,
        ('cup', 'tablespoon'): 16.0,
        ('cup', 'teaspoon'): 48.0,
        ('tablespoon', 'milliliter'): 14.787,
        ('tablespoon', 'liter'): 0.014787,
        ('tablespoon', 'gallon'): 0.00390625,
        ('tablespoon', 'cup'): 0.0625,
        ('tablespoon', 'teaspoon'): 3.0,
        ('teaspoon', 'milliliter'): 4.92892,
        ('teaspoon', 'liter'): 0.00492892,
        ('teaspoon', 'gallon'): 0.00130208,
        ('teaspoon', 'cup'): 0.0208333,
        ('teaspoon', 'tablespoon'): 0.333333,
    }

    from_lower = from_unit.lower()
    to_lower = to_unit.lower()

    if from_lower == to_lower:
        return volume

    factor = conversions.get((from_lower, to_lower))
    if factor is None:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")

    return volume * factor

def main():
    parser = argparse.ArgumentParser(description='Volume converter')
    parser.add_argument('--volume', type=float, required=True, help='Volume to convert')
    parser.add_argument('--from', dest='from_unit', type=str, required=True, help='Starting unit')
    parser.add_argument('--to', dest='to_unit', type=str, required=True, help='Target unit')

    args = parser.parse_args()

    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == '__main__':
    sample_result = convert_volume(1.0, 'liter', 'milliliter')
    print(sample_result)
    
    sample_result2 = convert_volume(32.0, 'cup', 'liter')
    print(sample_result2)
    
    sample_result3 = convert_volume(100.0, 'milliliter', 'gallon')
    print(sample_result3)