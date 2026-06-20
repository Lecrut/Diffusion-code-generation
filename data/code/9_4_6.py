import argparse

class VolumeConverter:
    def __init__(self):
        self.units = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon_us': 3.78541,
            'quart_us': 0.946353,
            'pint_us': 0.473176,
            'cup_us': 0.236588,
            'fluid_ounce_us': 0.0295735,
            'tablespoon_us': 0.0147868,
            'teaspoon_us': 0.00492892
        }

    def convert(self, volume, start_unit, target_unit):
        if start_unit not in self.units:
            raise ValueError(f"Unsupported start unit: {start_unit}")
        if target_unit not in self.units:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        volume_in_liters = volume * self.units[start_unit]
        converted_volume = volume_in_liters / self.units[target_unit]
        return converted_volume

def parse_arguments():
    parser = argparse.ArgumentParser(description='Convert volumes between different units.')
    parser.add_argument('volume', type=float, help='The volume value to convert')
    parser.add_argument('start_unit', type=str, help='The starting unit (e.g., liter, gallon_us)')
    parser.add_argument('target_unit', type=str, help='The target unit (e.g., milliliter, quart_us)')
    return parser.parse_args()

def run_conversion():
    args = parse_arguments()
    converter = VolumeConverter()
    result = converter.convert(args.volume, args.start_unit, args.target_unit)
    print(result)

if __name__ == '__main__':
    import sys
    original_argv = sys.argv
    sys.argv = ['script.py', '5.0', 'liter', 'gallon_us']
    converter_instance = VolumeConverter()
    result_value = converter_instance.convert(5.0, 'liter', 'gallon_us')
    print(result_value)
    sys.argv = original_argv