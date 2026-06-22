import argparse

def convert_volume(volume, from_unit, to_unit):
    conversions = {
        ('ml', 'ml'): 1,
        ('ml', 'l'): 0.001,
        ('ml', 'fl_oz'): 0.033814,
        ('ml', 'cup'): 0.00422675,
        ('l', 'ml'): 1000,
        ('l', 'l'): 1,
        ('l', 'fl_oz'): 33.814,
        ('l', 'cup'): 4.22675,
        ('fl_oz', 'ml'): 29.5735,
        ('fl_oz', 'l'): 0.0295735,
        ('fl_oz', 'fl_oz'): 1,
        ('fl_oz', 'cup'): 0.125,
        ('cup', 'ml'): 236.588,
        ('cup', 'l'): 0.236588,
        ('cup', 'fl_oz'): 8,
        ('cup', 'cup'): 1,
    }
    if (from_unit, to_unit) not in conversions:
        raise ValueError(f"Unsupported conversion from {from_unit} to {to_unit}")
    return volume * conversions[(from_unit, to_unit)]

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert volume between different units.')
    parser.add_argument('--volume', type=float, required=True, help='The volume to convert')
    parser.add_argument('--from-unit', type=str, required=True, choices=['ml', 'l', 'fl_oz', 'cup'], help='The starting unit')
    parser.add_argument('--to-unit', type=str, required=True, choices=['ml', 'l', 'fl_oz', 'cup'], help='The target unit')
    return parser.parse_args()

if __name__ == '__main__':
    args = parse_arguments()
    result = convert_volume(args.volume, args.from_unit, args.to_unit)
    print(result)