import argparse

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'liter': 1.0,
            'milliliter': 0.001,
            'gallon_us': 3.78541,
            'quart_us': 0.946353,
            'pint_us': 0.473176,
            'cup_us': 0.236588,
            'ounce_us': 0.0295735,
            'cubic_meter': 1000.0,
            'cubic_foot': 28.3168,
            'cubic_inch': 0.0163871
        }

    def convert(self, volume, start_unit, target_unit):
        if start_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported start unit: {start_unit}")
        if target_unit not in self.conversion_factors:
            raise ValueError(f"Unsupported target unit: {target_unit}")
        
        liters = volume * self.conversion_factors[start_unit]
        result = liters / self.conversion_factors[target_unit]
        return result

def main():
    parser = argparse.ArgumentParser(description='Convert volumes between different units.')
    parser.add_argument('--volume', type=float, required=True, help='The volume amount to convert')
    parser.add_argument('--from-unit', type=str, required=True, help='The starting unit (e.g., liter, gallon_us)')
    parser.add_argument('--to-unit', type=str, required=True, help='The target unit (e.g., milliliter, liter)')
    
    args = parser.parse_args()
    
    converter = VolumeConverter()
    result = converter.convert(args.volume, args.from_unit, args.to_unit)
    print(f"{args.volume} {args.from_unit} is equal to {result} {args.to_unit}")

if __name__ == '__main__':
    import sys
    sys.argv = ['script.py', '--volume', '10', '--from-unit', 'liter', '--to-unit', 'milliliter']
    main()