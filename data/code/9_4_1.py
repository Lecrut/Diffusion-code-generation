import argparse
import sys

class VolumeConverter:
    units = {
        'milliliter': 0.001,
        'liter': 1.0,
        'gallon_us': 3.78541,
        'quart_us': 0.946353,
        'pint_us': 0.473176,
        'cup_us': 0.236588,
        'fluid_ounce_us': 0.0295735
    }

    def __init__(self):
        self.parser = argparse.ArgumentParser(description='Convert volume between units.')
        self.parser.add_argument('volume', type=float, help='The volume value to convert')
        self.parser.add_argument('from_unit', choices=self.units.keys(), help='The starting unit')
        self.parser.add_argument('to_unit', choices=self.units.keys(), help='The target unit')

    def convert(self, volume, from_unit, to_unit):
        if from_unit not in self.units or to_unit not in self.units:
            raise ValueError('Invalid unit specified')
        base_volume = volume * self.units[from_unit]
        result_volume = base_volume / self.units[to_unit]
        return result_volume

def main():
    converter = VolumeConverter()
    args = converter.parser.parse_args(['10', 'liter', 'gallon_us'])
    result = converter.convert(args.volume, args.from_unit, args.to_unit)
    print(result)

if __name__ == '__main__':
    main()