import argparse
import sys

CONVERSION_MAP = {
    ('cubic_centimeter', 'milliliter'): 1.0,
    ('milliliter', 'cubic_centimeter'): 1.0,
    ('cubic_meter', 'liter'): 1000.0,
    ('liter', 'cubic_meter'): 0.001,
    ('cubic_meter', 'gallon_us'): 264.172,
    ('gallon_us', 'cubic_meter'): 1 / 264.172,
    ('liter', 'gallon_us'): 0.264172,
    ('gallon_us', 'liter'): 1 / 0.264172,
    ('cubic_centimeter', 'cup_us'): 0.00422675,
    ('cup_us', 'cubic_centimeter'): 1 / 0.00422675,
    ('liter', 'cup_us'): 4.22675,
    ('cup_us', 'liter'): 1 / 4.22675,
    ('cubic_meter', 'cup_us'): 4226.75,
    ('cup_us', 'cubic_meter'): 1 / 4226.75,
    ('cubic_meter', 'milliliter'): 1000000.0,
    ('milliliter', 'cubic_meter'): 1e-6,
    ('gallon_us', 'milliliter'): 3785.41,
    ('milliliter', 'gallon_us'): 1 / 3785.41,
    ('gallon_us', 'cubic_centimeter'): 3785.41,
    ('cubic_centimeter', 'gallon_us'): 1 / 3785.41,
    ('gallon_us', 'cup_us'): 16.0,
    ('cup_us', 'gallon_us'): 1 / 16.0,
    ('gallon_us', 'liter'): 3.78541,
    ('liter', 'gallon_us'): 0.264172,
    ('liter', 'milliliter'): 1000.0,
    ('milliliter', 'liter'): 0.001,
    ('cubic_meter', 'cubic_centimeter'): 1000000.0,
    ('cubic_centimeter', 'cubic_meter'): 1e-6,
}

VALID_UNITS = ['cubic_centimeter', 'milliliter', 'cubic_meter', 'liter', 'gallon_us', 'cup_us']

def parse_arguments():
    parser = argparse.ArgumentParser(description='Volume Unit Converter')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('start_unit', type=str, help='The starting unit of measurement')
    parser.add_argument('target_unit', type=str, help='The target unit of measurement')
    return parser.parse_args()

def convert_volume(volume, start_unit, target_unit):
    if start_unit not in VALID_UNITS:
        raise ValueError(f"Invalid start unit: {start_unit}")
    if target_unit not in VALID_UNITS:
        raise ValueError(f"Invalid target unit: {target_unit}")
    if start_unit == target_unit:
        return volume
    
    key = (start_unit, target_unit)
    if key in CONVERSION_MAP:
        return volume * CONVERSION_MAP[key]
    
    raise ValueError(f"Conversion from {start_unit} to {target_unit} is not directly supported.")

def main():
    args = parse_arguments()
    result = convert_volume(args.volume, args.start_unit, args.target_unit)
    print(result)

if __name__ == '__main__':
    main()