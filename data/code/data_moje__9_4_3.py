import argparse
import sys

class VolumeConverter:
    def __init__(self):
        self.units = {
            'l': 1.0,
            'ml': 0.001,
            'gal': 3.78541,
            'qt': 0.946353,
            'pt': 0.473176,
            'cup': 0.236588,
            'fl_oz': 0.0295735,
            'tbsp': 0.0147868,
            'tsp': 0.00492892,
            'm3': 1000.0,
            'cm3': 0.001
        }

    def convert(self, volume, from_unit, to_unit):
        from_unit_lower = from_unit.lower()
        to_unit_lower = to_unit.lower()
        
        if from_unit_lower not in self.units:
            raise ValueError(f"Invalid starting unit: {from_unit}")
        if to_unit_lower not in self.units:
            raise ValueError(f"Invalid target unit: {to_unit}")
        
        volume_in_liters = volume * self.units[from_unit_lower]
        result = volume_in_liters / self.units[to_unit_lower]
        return result

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert volume between units')
    parser.add_argument('--volume', type=float, default=1.0, help='Volume to convert')
    parser.add_argument('--from', dest='from_unit', type=str, default='l', help='Starting unit')
    parser.add_argument('--to', dest='to_unit', type=str, default='gal', help='Target unit')
    return parser.parse_args([])

def run_conversion():
    args = parse_arguments()
    converter = VolumeConverter()
    result = converter.convert(args.volume, args.from_unit, args.to_unit)
    return result

if __name__ == '__main__':
    output = run_conversion()
    print(f"Result: {output}")