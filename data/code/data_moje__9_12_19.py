import argparse
import sys

class VolumeConverter:
    def __init__(self):
        self.conversion_factors = {
            'milliliter': 1.0,
            'ml': 1.0,
            'liter': 1000.0,
            'l': 1000.0,
            'gallon': 3785.41,
            'gal': 3785.41,
            'quart': 946.353,
            'qt': 946.353,
            'pint': 473.176,
            'pt': 473.176,
            'cup': 236.588,
            'fluid_ounce': 29.5735,
            'floz': 29.5735,
        }

    def convert(self, value, input_unit, output_unit):
        if value < 0:
            raise ValueError("Volume cannot be negative")
        
        if input_unit not in self.conversion_factors:
            raise ValueError(f"Invalid input unit: {input_unit}")
        
        if output_unit not in self.conversion_factors:
            raise ValueError(f"Invalid output unit: {output_unit}")
        
        base_ml = value * self.conversion_factors[input_unit]
        result = base_ml / self.conversion_factors[output_unit]
        return result

def main():
    parser = argparse.ArgumentParser(description='Convert volume units')
    parser.add_argument('--input-volume', type=float, default=1.0, help='Input volume value')
    parser.add_argument('--input-unit', type=str, default='gallon', help='Input unit')
    parser.add_argument('--output-unit', type=str, default='liter', help='Output unit')
    
    args = parser.parse_args()
    
    converter = VolumeConverter()
    
    try:
        result = converter.convert(args.input_volume, args.input_unit, args.output_unit)
        print(f"{args.input_volume} {args.input_unit} is {result:.4f} {args.output_unit}")
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

if __name__ == '__main__':
    main()